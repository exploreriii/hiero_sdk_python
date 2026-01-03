/**
 * Determines whether a contributor is eligible to be assigned
 * a Beginner issue in this repository.
 *
 * ELIGIBILITY RULES:
 * - Repository team members (triage / write / maintain / admin)
 *   bypass all eligibility and capacity checks.
 * - Contributors on the spam list are never eligible.
 * - Contributors must have completed at least `REQUIRED_GFI_COUNT`
 *   Good First Issues.
 * - Contributors may have fewer than `MAX_OPEN_ASSIGNED_ISSUES`
 *   open issue assignments.
 *
 * IMPORTANT NOTES:
 * - This helper is policy-only.
 * - It does NOT assign issues.
 * - It does NOT post comments.
 * - Callers must invoke this before attempting assignment.
 *
 * FAILURE BEHAVIOR:
 * - Relies on downstream helpers that fail open.
 * - If assignment counts cannot be determined, this helper
 *   conservatively returns `false`.
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github - Authenticated GitHub client
 * @param {string} params.owner - Repository owner
 * @param {string} params.repo - Repository name
 * @param {string} params.username - GitHub username to check
 * @returns {Promise<boolean>} Whether the contributor may be assigned a Beginner issue
 */
const { isTeam } = require('./is-team');
const { isOnSpamList } = require('../counts/is-on-spam-list');
const { hasCompletedGfi } = require('./has-gfi');
const { countOpenAssignedIssues } = require('../counts/count-open-assigned-issues');

/**
 * Maximum number of open issues allowed for Beginner eligibility.
 *
 * This value represents a policy decision and must stay in sync
 * with guard messaging and documentation.
 */
const MAX_OPEN_ASSIGNED_ISSUES = 2;

/**
 * Number of Good First Issues required to qualify for Beginner issues.
 *
 * Expressed explicitly to keep policy decisions out of helpers.
 */
const REQUIRED_GFI_COUNT = 1;

const hasBeginnerEligibility = async ({
    github,
    owner,
    repo,
    username,
}) => {
    // Log the start of the eligibility check for traceability
    console.log('[has-beginner-eligibility] Start check:', {
        owner,
        repo,
        username,
    });

    // Repository team members bypass all Beginner eligibility checks.
    if (await isTeam({ github, owner, repo, username })) {
        console.log('[has-beginner-eligibility] Skipped: user is team member', {
            username,
        });
        return true;
    }

    // Contributors on the spam list are never eligible for Beginner issues.
    if (await isOnSpamList({ github, owner, repo, username })) {
        console.log('[has-beginner-eligibility] Exit: user is on spam list', {
            username,
        });
        return false;
    }

    // Enforce capacity limits for open issue assignments.
    // This helper fails open and returns a large number on error,
    // which conservatively blocks assignment.
    const openAssignedCount = await countOpenAssignedIssues({
        github,
        owner,
        repo,
        username,
    });

    if (openAssignedCount >= MAX_OPEN_ASSIGNED_ISSUES) {
        console.log('[has-beginner-eligibility] Exit: assignment limit reached', {
            username,
            openAssignedCount,
            maxAllowed: MAX_OPEN_ASSIGNED_ISSUES,
        });
        return false;
    }

    // Verify Good First Issue completion requirement.
    const hasRequiredGfi = await hasCompletedGfi({
        github,
        owner,
        repo,
        username,
        requiredCount: REQUIRED_GFI_COUNT,
    });

    if (!hasRequiredGfi) {
        console.log('[has-beginner-eligibility] Exit: missing GFI completion', {
            username,
            requiredCount: REQUIRED_GFI_COUNT,
        });
        return false;
    }

    // Contributor meets all Beginner eligibility requirements.
    console.log('[has-beginner-eligibility] Success: contributor eligible for Beginner issues', {
        username,
    });

    return true;
};

module.exports = {
    hasBeginnerEligibility,
};
