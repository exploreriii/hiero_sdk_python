/**
 * Determines whether a contributor is eligible to be assigned
 * an Intermediate issue.
 *
 * ELIGIBILITY RULES:
 * - Team members bypass all checks
 * - Spam-listed users are never eligible
 * - Max N open assignments allowed
 * - Must have completed REQUIRED_BEGINNER_COUNT Beginner issues
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

const { isTeam } = require('../team/has-team');
const { isOnSpamList } = require('../counts/is-on-spam-list');
const { hasCompletedBeginner } =
    require('../counts/has-completed-n-02-beginner');
const { countOpenAssignedIssues } =
    require('../counts/count-opened-assigned-issues');
const REJECTION_REASONS =
    require('./rejection-reasons');

// ─────────────────────────────────────────────
// Policy configuration
// ─────────────────────────────────────────────
const MAX_OPEN_ASSIGNED_ISSUES = 2;
const REQUIRED_BEGINNER_COUNT = 1;

const hasIntermediateEligibility = async ({
    github,
    owner,
    repo,
    username,
}) => {
    console.log('[has-intermediate-eligibility] Start', {
        owner,
        repo,
        username,
    });

    // ─────────────────────────────────────────────
    // Team members bypass everything
    // ─────────────────────────────────────────────
    if (await isTeam({ github, owner, repo, username })) {
        console.log('[has-intermediate-eligibility] Bypass: team member', {
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
        console.log('[has-intermediate-eligibility] Rejected: spam listed', {
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

    console.log('[has-intermediate-eligibility] Capacity evaluation', {
        username,
        openAssignedCount,
        maxAllowed: MAX_OPEN_ASSIGNED_ISSUES,
    });

    if (openAssignedCount >= MAX_OPEN_ASSIGNED_ISSUES) {
        console.log('[has-intermediate-eligibility] Rejected: capacity exceeded', {
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
    // Beginner prerequisite
    // ─────────────────────────────────────────────
    const hasRequiredBeginner = await hasCompletedBeginner({
        github,
        owner,
        repo,
        username,
        requiredCount: REQUIRED_BEGINNER_COUNT,
    });

    console.log('[has-intermediate-eligibility] Beginner prerequisite', {
        username,
        hasRequiredBeginner,
        requiredCount: REQUIRED_BEGINNER_COUNT,
    });

    if (!hasRequiredBeginner) {
        console.log('[has-intermediate-eligibility] Rejected: missing beginner', {
            username,
        });

        return {
            eligible: false,
            reason: REJECTION_REASONS.MISSING_BEGINNER,
            context: {
                requiredBeginnerCount: REQUIRED_BEGINNER_COUNT,
            },
        };
    }

    // ─────────────────────────────────────────────
    // Eligible
    // ─────────────────────────────────────────────
    console.log('[has-intermediate-eligibility] Eligible', {
        username,
    });

    return { eligible: true };
};

module.exports = {
    hasIntermediateEligibility,
};
