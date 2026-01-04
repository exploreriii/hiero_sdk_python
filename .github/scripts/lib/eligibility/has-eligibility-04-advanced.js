/**
 * Determines whether a contributor is eligible to be assigned
 * an Advanced issue.
 *
 * ELIGIBILITY RULES:
 * - Committers / maintainers bypass all checks
 * - Spam-listed users are never eligible
 * - Max N open assignments allowed
 * - Must have completed REQUIRED_INTERMEDIATE_COUNT Intermediate issues
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github
 * @param {string} params.owner
 * @param {string} params.repo
 * @param {string} params.username
 * @returns {Promise<{
 *   eligible: boolean,
 *   reason?: string,
 *   context?: Object
 * }>}
 */

const { isCommitter } =
    require('../team/has-team-committer-maintainer');
const { isOnSpamList } =
    require('../counts/is-on-spam-list');
const { hasCompletedIntermediate } =
    require('../counts/has-completed-n-03-intermediate');
const { countOpenAssignedIssues } =
    require('../counts/count-opened-assigned-issues');
const REJECTION_REASONS =
    require('./rejection-reasons');

// ─────────────────────────────────────────────
// Policy configuration
// ─────────────────────────────────────────────
const MAX_OPEN_ASSIGNED_ISSUES = 2;
const REQUIRED_INTERMEDIATE_COUNT = 1;

const hasAdvancedEligibility = async ({
    github,
    owner,
    repo,
    username,
}) => {
    console.log('[has-advanced-eligibility] Start', {
        owner,
        repo,
        username,
    });

    // ─────────────────────────────────────────────
    // Committers / maintainers bypass all checks
    // ─────────────────────────────────────────────
    if (await isCommitter({ github, owner, repo, username })) {
        console.log('[has-advanced-eligibility] Bypass: committer', {
            username,
        });

        return { eligible: true };
    }

    // ─────────────────────────────────────────────
    // Spam-listed users are never eligible
    // ─────────────────────────────────────────────
    const isSpamListed = await isOnSpamList({
        github,
        owner,
        repo,
        username,
    });

    if (isSpamListed) {
        console.log('[has-advanced-eligibility] Rejected: spam listed', {
            username,
        });

        return {
            eligible: false,
            reason: REJECTION_REASONS.SPAM,
        };
    }

    // ─────────────────────────────────────────────
    // Capacity check
    // ─────────────────────────────────────────────
    const openAssignedCount = await countOpenAssignedIssues({
        github,
        owner,
        repo,
        username,
    });

    console.log('[has-advanced-eligibility] Capacity evaluation', {
        username,
        openAssignedCount,
        maxAllowed: MAX_OPEN_ASSIGNED_ISSUES,
    });

    if (openAssignedCount >= MAX_OPEN_ASSIGNED_ISSUES) {
        console.log('[has-advanced-eligibility] Rejected: capacity exceeded', {
            username,
        });

        return {
            eligible: false,
            reason: REJECTION_REASONS.CAPACITY,
            context: {
                openAssignedCount,
                maxAllowed: MAX_OPEN_ASSIGNED_ISSUES,
            },
        };
    }

    // ─────────────────────────────────────────────
    // Intermediate prerequisite
    // ─────────────────────────────────────────────
    const hasRequiredIntermediate =
        await hasCompletedIntermediate({
            github,
            owner,
            repo,
            username,
            requiredCount: REQUIRED_INTERMEDIATE_COUNT,
        });

    console.log('[has-advanced-eligibility] Intermediate prerequisite', {
        username,
        hasRequiredIntermediate,
        requiredCount: REQUIRED_INTERMEDIATE_COUNT,
    });

    if (!hasRequiredIntermediate) {
        console.log(
            '[has-advanced-eligibility] Rejected: missing intermediate',
            { username }
        );

        return {
            eligible: false,
            reason: REJECTION_REASONS.MISSING_INTERMEDIATE,
            context: {
                requiredIntermediateCount: REQUIRED_INTERMEDIATE_COUNT,
            },
        };
    }

    // ─────────────────────────────────────────────
    // Eligible
    // ─────────────────────────────────────────────
    console.log('[has-advanced-eligibility] Eligible', {
        username,
    });

    return { eligible: true };
};

module.exports = {
    hasAdvancedEligibility,
};
