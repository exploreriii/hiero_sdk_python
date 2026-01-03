/**
 * Determines whether a contributor is eligible to be assigned
 * an Advanced issue in this repository.
 *
 * ELIGIBILITY RULES:
 * - Committers (write / maintain / admin) bypass all eligibility
 *   checks and capacity limits.
 * - Contributors on the spam list are never eligible.
 * - Contributors must have completed at least
 *   `REQUIRED_INTERMEDIATE_COUNT` Intermediate issues.
 * - Contributors may have fewer than `MAX_OPEN_ASSIGNED_ISSUES`
 *   open issue assignments.
 *
 * IMPORTANT NOTES:
 * - Triage members are NOT exempt and must meet all requirements.
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
 * @returns {Promise<boolean>} Whether the contributor may be assigned an Advanced issue
 */
const { isCommitter } = require('..team/has-team-committer-maintainer');
const { isOnSpamList } = require('../counts/is-on-spam-list');
const { hasCompletedIntermediate } = require('../counts/has-completed-n-03-intermediate');
const { countOpenAssignedIssues } = require('../counts/count-open-assigned-issues');

/**
 * Maximum number of open issues allowed for Advanced eligibility.
 *
 * This value represents a policy decision and should be kept
 * in sync with guard messaging and documentation.
 */
const MAX_OPEN_ASSIGNED_ISSUES = 2;

/**
 * Number of completed Intermediate issues required
 * to qualify for Advanced issues.
 */
const REQUIRED_INTERMEDIATE_COUNT = 2;

const hasAdvancedEligibility = async ({
    github,
    owner,
    repo,
    username,
}) => {
    // Log the start of the eligibility check for traceability
    console.log('[has-advanced-eligibility] Start check:', {
        owner,
        repo,
        username,
    });

    // Committers bypass all Advanced eligibility checks.
    if (await isCommitter({ github, owner, repo, username })) {
        console.log('[has-advanced-eligibility] Skipped: user is committer', {
            username,
        });
        return true;
    }

    // Contributors on the spam list are never eligible.
    if (await isOnSpamList({ github, owner, repo, username })) {
        console.log('[has-advanced-eligibility] Exit: user is on spam list', {
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
        console.log('[has-advanced-eligibility] Exit: assignment limit reached', {
            username,
            openAssignedCount,
            maxAllowed: MAX_OPEN_ASSIGNED_ISSUES,
        });
        return false;
    }

    // Verify Intermediate issue completion requirement.
    const hasRequiredIntermediate = await hasCompletedIntermediate({
        github,
        owner,
        repo,
        username,
        requiredCount: REQUIRED_INTERMEDIATE_COUNT,
    });

    if (!hasRequiredIntermediate) {
        console.log(
            '[has-advanced-eligibility] Exit: missing required Intermediate completions',
            {
                username,
                requiredCount: REQUIRED_INTERMEDIATE_COUNT,
            }
        );
        return false;
    }

    // Contributor meets all Advanced eligibility requirements.
    console.log(
        '[has-advanced-eligibility] Success: contributor eligible for Advanced issues',
        { username }
    );

    return true;
};

module.exports = {
    hasAdvancedEligibility,
};
