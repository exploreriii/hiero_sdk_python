const { isTeam } = require('../team/has-team');
const { isOnSpamList } = require('../counts/is-on-spam-list');
const { hasCompletedGfi } = require('../counts/has-completed-n-01-gfi');
const { countOpenAssignedIssues } = require('../counts/count-open-assigned-issues');
const REJECTION_REASONS = require('./rejection-reasons');

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

    // Team members bypass everything
    if (await isTeam({ github, owner, repo, username })) {
        return { eligible: true };
    }

    // Spam-listed users are never eligible
    if (await isOnSpamList({ github, owner, repo, username })) {
        return {
            eligible: false,
            reason: REJECTION_REASONS.SPAM,
        };
    }

    // Capacity check
    const openAssignedCount = await countOpenAssignedIssues({
        github,
        owner,
        repo,
        username,
    });

    if (openAssignedCount >= MAX_OPEN_ASSIGNED_ISSUES) {
        return {
            eligible: false,
            reason: REJECTION_REASONS.CAPACITY,
            context: {
                openAssignedCount,
                maxAllowed: MAX_OPEN_ASSIGNED_ISSUES,
            },
        };
    }

    // GFI prerequisite
    const hasRequiredGfi = await hasCompletedGfi({
        github,
        owner,
        repo,
        username,
        requiredCount: REQUIRED_GFI_COUNT,
    });

    if (!hasRequiredGfi) {
        return {
            eligible: false,
            reason: REJECTION_REASONS.MISSING_GFI,
            context: {
                completedGfiCount: 0, // safe fallback
            },
        };
    }

    return { eligible: true };
};

module.exports = { hasBeginnerEligibility };

