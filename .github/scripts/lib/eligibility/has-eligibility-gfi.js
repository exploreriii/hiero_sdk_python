// Reusable function to check if a user is eligible to be assigned
// a Good First Issue.
//
// Eligibility requirements:
// - Normal users may have up to 2 open assigned issues.
// - Users on the spam list may have up to 1 open assigned issue.
// - Assignment is allowed only if the user currently has fewer than
//   their allowed maximum.
//
// NOTES:
// - This helper is policy-only.
// - It does NOT assign issues or post comments.
// - Bots should call this before attempting assignment.

const { countOpenAssignedIssues } = require('./count-open-assigned-issues');
const { isOnSpamList } = require('../counts/is-on-spam-list');

const MAX_OPEN_ISSUES_NORMAL = 2;
const MAX_OPEN_ISSUES_SPAM_LIST = 1;

async function hasGfiEligibility({ github, owner, repo, username }) {
    console.log('[has-gfi-eligibility] Start check:', {
        owner,
        repo,
        username,
    });

    const isSpamListed = await isOnSpamList({
        github,
        owner,
        repo,
        username,
    });

    const maxAllowed = isSpamListed
        ? MAX_OPEN_ISSUES_SPAM_LIST
        : MAX_OPEN_ISSUES_NORMAL;

    const openAssignedCount = await countOpenAssignedIssues({
        github,
        owner,
        repo,
        username,
    });

    console.log('[has-gfi-eligibility] Capacity check:', {
        username,
        isSpamListed,
        openAssignedCount,
        maxAllowed,
    });

    if (openAssignedCount >= maxAllowed) {
        console.log('[has-gfi-eligibility] Exit: assignment limit reached', {
            username,
        });
        return false;
    }

    console.log('[has-gfi-eligibility] Success: user may be assigned GFI', {
        username,
    });

    return true;
}

module.exports = {
    hasGfiEligibility,
};
