/**
 * Determines whether a contributor is eligible to be assigned
 * an Intermediate issue in this repository.
 *
 * ELIGIBILITY RULES (for non-triage contributors):
 * - Contributors on the spam list are never eligible.
 * - Contributors must have completed at least:
 *   - `REQUIRED_GFI_COUNT` Good First Issues
 *   - `REQUIRED_BEGINNER_COUNT` Beginner issues
 * - Contributors may have fewer than `MAX_OPEN_ASSIGNED_ISSUES`
 *   open issue assignments.
 *
 * EXEMPTION RULE:
 * - Triage members and above (triage / write / maintain / admin)
 *   bypass all eligibility checks and capacity limits.
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
 * @returns {Promise<boolean>} Whether the contributor may be assigned an Intermediate issue
 */
const { isTriager } = require('./is-triager');
const { isOnSpamList } = require('../counts/is-on-spam-list');
const { hasCompletedGfi } = require('./has-gfi');
const { hasCompletedBeginner } = require('./has-beginner');
const { countOpenAssignedIssues } = require('./count-open-assigned-issues');

/**
 * Maximum number of open issues allowed for Intermediate eligibility.
 *
 * This value represents a policy decision and should be kept
 * in sync with guard messaging and documentation.
 */
const MAX_OPEN_ASSIGNED_ISSUES = 2;

/**
 * Number of completed Good First Issues required
 * to qualify for Intermediate issues.
 */
const REQUIRED_GFI_COUNT = 1;

/**
 * Number of completed Beginner issues required
 * to qualify for Intermediate issues.
 */
const REQUIRED_BEGINNER_COUNT = 1;

const hasIntermediateEligibility = async ({
    github,
    owner,
    repo,
    username,
}) => {
    // Log the start of the eligibility check for traceability
    console.log('[has-intermediate-eligibility] Start check:', {
        owner,
        repo,
        username,
    });

    // Contributors on the spam list are never eligible
    if (await isOnSpamList({ github, owner, repo, username })) {
        console.log('[has-intermediate-eligibility] Exit: user is on spam list', {
            username,
        });
        return false;
    }

    // Triage members and above bypass all eligibility checks
    if (await isTriager({ github, owner, repo, username })) {
        console.log('[has-intermediate-eligibility] Skipped: user is triage+', {
            username,
        });
        return true;
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
        console.log('[has-intermediate-eligibility] Exit: assignment limit reached', {
            username,
            openAssignedCount,
            maxAllowed: MAX_OPEN_ASSIGNED_ISSUES,
        });
        return false;
    }

    // Verify Good First Issue completion requirement
    const hasRequiredGfi = await hasCompletedGfi({
        github,
        owner,
        repo,
        username,
        requiredCount: REQUIRED_GFI_COUNT,
    });

    if (!hasRequiredGfi) {
        console.log('[has-intermediate-eligibility] Exit: missing GFI completion', {
            username,
            requiredCount: REQUIRED_GFI_COUNT,
        });
        return false;
    }

    // Verify Beginner Issue completion requirement
    const hasRequiredBeginner = await hasCompletedBeginner({
        github,
        owner,
        repo,
        username,
        requiredCount: REQUIRED_BEGINNER_COUNT,
    });

    if (!hasRequiredBeginner) {
        console.log('[has-intermediate-eligibility] Exit: missing Beginner completion', {
            username,
            requiredCount: REQUIRED_BEGINNER_COUNT,
        });
        return false;
    }

    // Contributor meets all Intermediate eligibility requirements
    console.log('[has-intermediate-eligibility] Success: contributor eligible for Intermediate issues', {
        username,
    });

    return true;
};

module.exports = {
    hasIntermediateEligibility,
};
