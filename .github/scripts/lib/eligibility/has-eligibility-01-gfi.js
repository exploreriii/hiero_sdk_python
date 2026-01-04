/**
 * Determines whether a contributor is eligible to be assigned
 * a Good First Issue (GFI).
 *
 * ELIGIBILITY RULES:
 * - Repository team members (triage / write / maintain / admin)
 *   always bypass GFI eligibility checks.
 * - Spam-listed contributors may have at most
 *   `MAX_OPEN_ISSUES_SPAM_LIST` open GFI assignments.
 * - All other contributors may have at most
 *   `MAX_OPEN_ISSUES_NORMAL` open GFI assignments.
 *
 * IMPORTANT:
 * - This helper is policy-only.
 * - It does NOT assign issues.
 * - It does NOT post comments.
 * - Callers must route rejections via `rejectionRouter`.
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
const { countOpenAssignedIssues } =
    require('../counts/count-opened-assigned-issues');
const REJECTION_REASONS = require('./rejection-reasons');

// ─────────────────────────────────────────────
// Policy configuration
// ─────────────────────────────────────────────
const MAX_OPEN_ISSUES_NORMAL = 2;
const MAX_OPEN_ISSUES_SPAM_LIST = 1;

const hasGfiEligibility = async ({
    github,
    owner,
    repo,
    username,
}) => {
    console.log('[has-gfi-eligibility] Start', {
        owner,
        repo,
        username,
    });

    // ─────────────────────────────────────────────
    // Team members bypass all GFI restrictions
    // ─────────────────────────────────────────────
    if (await isTeam({ github, owner, repo, username })) {
        console.log('[has-gfi-eligibility] Bypass: team member', {
            username,
        });

        return { eligible: true };
    }

    // ─────────────────────────────────────────────
    // Spam list evaluation
    // ─────────────────────────────────────────────
    const isSpamListed = await isOnSpamList({
        github,
        owner,
        repo,
        username,
    });

    const maxAllowed = isSpamListed
        ? MAX_OPEN_ISSUES_SPAM_LIST
        : MAX_OPEN_ISSUES_NORMAL;

    // ─────────────────────────────────────────────
    // Capacity check
    // ─────────────────────────────────────────────
    const openAssignedCount = await countOpenAssignedIssues({
        github,
        owner,
        repo,
        username,
    });

    console.log('[has-gfi-eligibility] Capacity evaluation', {
        username,
        isSpamListed,
        openAssignedCount,
        maxAllowed,
    });

    if (openAssignedCount >= maxAllowed) {
        console.log('[has-gfi-eligibility] Rejected: capacity exceeded', {
            username,
        });

        return {
            eligible: false,
            reason: REJECTION_REASONS.CAPACITY,
            context: {
                openAssignedCount,
                maxAllowed,
                isSpamListed,
            },
        };
    }

    // ─────────────────────────────────────────────
    // Eligible
    // ─────────────────────────────────────────────
    console.log('[has-gfi-eligibility] Eligible', {
        username,
    });

    return { eligible: true };
};

module.exports = { hasGfiEligibility };
