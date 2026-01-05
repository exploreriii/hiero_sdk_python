/**
 * Determines whether a contributor is eligible to be assigned
 * a Beginner issue.
 *
 * ELIGIBILITY RULES:
 * - Team members bypass all checks
 * - Spam-listed users are never eligible
 * - Max open assignments enforced
 * - Must have completed at least N Good First Issues
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
const { hasCompletedGfi } =
    require('../counts/has-completed-n-01-gfi');
const { countOpenAssignedIssues } =
    require('../counts/count-opened-assigned-issues');
const REJECTION_REASONS = require('./rejection-reasons');

// ─────────────────────────────────────────────
// Policy configuration
// ─────────────────────────────────────────────
const MAX_OPEN_ASSIGNED_ISSUES = 2;
const REQUIRED_GFI_COUNT = 1;

const hasBeginnerEligibility = async ({
    github,
    owner,
    repo,
    username,
}) => {
    console.log('[has-beginner-eligibility] Start', {
        owner,
        repo,
        username,
    });

    // ─────────────────────────────────────────────
    // Team members bypass everything
    // ─────────────────────────────────────────────
    if (await isTeam({ github, owner, repo, username })) {
        console.log('[has-beginner-eligibility] Bypass: team member', {
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
        console.log('[has-beginner-eligibility] Rejected: spam listed', {
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

    console.log('[has-beginner-eligibility] Capacity evaluation', {
        username,
        openAssignedCount,
        maxAllowed: MAX_OPEN_ASSIGNED_ISSUES,
    });

    if (openAssignedCount >= MAX_OPEN_ASSIGNED_ISSUES) {
        console.log('[has-beginner-eligibility] Rejected: capacity exceeded', {
            username,
        });

        return {
            eligible: false,
            reason: REJECTION_REASONS.CAPACITY,
            context: {
                openAssignedCount,
                maxAllowed: MAX_OPEN_ASSIGNED_ISSUES,
                isSpamListed: false,
            },
        };
    }

    // ─────────────────────────────────────────────
    // GFI prerequisite
    // ─────────────────────────────────────────────
    const hasRequiredGfi = await hasCompletedGfi({
        github,
        owner,
        repo,
        username,
        requiredCount: REQUIRED_GFI_COUNT,
    });

    console.log('[has-beginner-eligibility] GFI prerequisite', {
        username,
        requiredGfiCount: REQUIRED_GFI_COUNT,
        satisfied: hasRequiredGfi,
    });

    if (!hasRequiredGfi) {
        console.log('[has-beginner-eligibility] Rejected: missing GFI', {
            username,
        });

        return {
            eligible: false,
            reason: REJECTION_REASONS.MISSING_GFI,
            context: {
                completedGfiCount: 0,
                requiredGfiCount: REQUIRED_GFI_COUNT,
            },
        };
    }

    // ─────────────────────────────────────────────
    // Eligible
    // ─────────────────────────────────────────────
    console.log('[has-beginner-eligibility] Eligible', {
        username,
    });

    return { eligible: true };
};

module.exports = { hasBeginnerEligibility };
