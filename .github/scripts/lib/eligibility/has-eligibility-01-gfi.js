const { isTeam } = require('../team/has-team');
const { isOnSpamList } = require('../counts/is-on-spam-list');
const { countOpenAssignedIssues } = require('../counts/count-open-assigned-issues');
const REJECTION_REASONS = require('./rejection-reasons');

const MAX_OPEN_ISSUES_NORMAL = 2;
const MAX_OPEN_ISSUES_SPAM_LIST = 1;

const hasGfiEligibility = async ({
    github,
    owner,
    repo,
    username,
}) => {
    if (await isTeam({ github, owner, repo, username })) {
        return { eligible: true };
    }

    const isSpamListed = await isOnSpamList({ github, owner, repo, username });

    const maxAllowed = isSpamListed
        ? MAX_OPEN_ISSUES_SPAM_LIST
        : MAX_OPEN_ISSUES_NORMAL;

    const openAssignedCount = await countOpenAssignedIssues({
        github,
        owner,
        repo,
        username,
    });

    if (openAssignedCount >= maxAllowed) {
        return {
            eligible: false,
            reason: REJECTION_REASONS.CAPACITY,
            context: { openAssignedCount, maxAllowed },
        };
    }

    return { eligible: true };
};

module.exports = { hasGfiEligibility };
