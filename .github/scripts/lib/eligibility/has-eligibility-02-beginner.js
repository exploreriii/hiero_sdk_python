/**
 * Determines whether a contributor is eligible to be assigned
 * a Beginner issue in this repository.
 *
 * ELIGIBILITY RULES:
 * - Committers (write / maintain / admin) bypass all checks.
 * - Contributors on the spam list are never eligible.
 * - Contributors must have completed at least one Good First Issue.
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
const { isCommitter } = require('./is-committer');
const { isOnSpamList } = require('../counts/is-on-spam-list');
const { hasCompletedGfi } = require('./has-gfi');
const { countOpenAssignedIssues } = require('./count-open-assigned-issues');

/**
 * Maximum number of open issues allowed for Beginner eligibility.
 *
 * This value represents a policy decision and should be kept in sync
 * with guard messaging and documentation.
 */
const MAX_OPEN_ASSIGNED_ISSUES = 2;

/**
 * Number of Good First Issues required to qualify for Beginner issues.
 *
 * Expressed here explicitly to keep policy decisions out of helpers.
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

    // Committers bypass all Beginner eligibility checks.
    if (await isCommitter({ github, owner, repo, username })) {
        console.log('[has-beginner-eligibility] Skipped: user is committer', {
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
    // This helper fails open, returning a large number on error,
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

    // Verify that the contributor has completed the required number
    // of Good First Issues.
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
