/**
 * Determines whether a contributor is eligible to be assigned
 * a Good First Issue (GFI) in this repository.
 *
 * ELIGIBILITY RULES:
 * - Normal contributors may have up to `MAX_OPEN_ISSUES_NORMAL`
 *   open issue assignments.
 * - Contributors listed in the spam list may have up to
 *   `MAX_OPEN_ISSUES_SPAM_LIST` open issue assignments.
 * - Assignment is allowed only if the contributor currently has
 *   fewer than their maximum allowed open assignments.
 *
 * IMPORTANT NOTES:
 * - This helper is policy-only.
 * - It does NOT assign issues.
 * - It does NOT post comments.
 * - Callers must invoke this before attempting assignment.
 *
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github - Authenticated GitHub client
 * @param {string} params.owner - Repository owner
 * @param {string} params.repo - Repository name
 * @param {string} params.username - GitHub username to check
 * @returns {Promise<boolean>} Whether the contributor may be assigned a GFI
 */
const { countOpenAssignedIssues } = require('..counts/count-open-assigned-issues');
const { isOnSpamList } = require('../counts/is-on-spam-list');

const MAX_OPEN_ISSUES_NORMAL = 2;
const MAX_OPEN_ISSUES_SPAM_LIST = 1;

const hasGfiEligibility = async ({
    github,
    owner,
    repo,
    username,
}) => {
    // Log the start of the eligibility check for traceability
    console.log('[has-gfi-eligibility] Start check:', {
        owner,
        repo,
        username,
    });

    // Determine whether the contributor is listed in the spam list.
    // Spam-listed contributors are subject to stricter limits.
    const isSpamListed = await isOnSpamList({
        github,
        owner,
        repo,
        username,
    });

    // Select the appropriate maximum based on spam status.
    const maxAllowed = isSpamListed
        ? MAX_OPEN_ISSUES_SPAM_LIST
        : MAX_OPEN_ISSUES_NORMAL;

    // Count how many open issues are currently assigned to the contributor.
    // This helper fails open and returns a large number on error,
    // which causes this eligibility check to conservatively fail.
    const openAssignedCount = await countOpenAssignedIssues({
        github,
        owner,
        repo,
        username,
    });

    console.log('[has-gfi-eligibility] Capacity evaluation:', {
        username,
        isSpamListed,
        openAssignedCount,
        maxAllowed,
    });

    // If the contributor has reached or exceeded their allowed capacity,
    // they are not eligible for assignment.
    if (openAssignedCount >= maxAllowed) {
        console.log('[has-gfi-eligibility] Exit: assignment limit reached', {
            username,
        });
        return false;
    }

    // Contributor is under their assignment limit and may be assigned a GFI.
    console.log('[has-gfi-eligibility] Success: contributor eligible for GFI', {
        username,
    });

    return true;
};

module.exports = {
    hasGfiEligibility,
};
