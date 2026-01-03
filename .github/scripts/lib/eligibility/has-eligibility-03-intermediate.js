const { isTeam } = require('../team/has-team');
const { isOnSpamList } = require('../counts/is-on-spam-list');
const { hasCompletedGfi } = require('../counts/has-completed-n-01-gfi');
const { hasCompletedBeginner } = require('../counts/has-completed-n-02-beginner');
const { countOpenAssignedIssues } = require('../counts/count-open-assigned-issues');
const REJECTION_REASONS = require('./rejection-reasons');

const MAX_OPEN_ASSIGNED_ISSUES = 2;
const REQUIRED_GFI_COUNT = 1;
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

    // GFI requirement
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
                requiredCount: REQUIRED_GFI_COUNT,
            },
        };
    }

    // Beginner requirement
    const hasRequiredBeginner = await hasCompletedBeginner({
        github,
        owner,
        repo,
        username,
        requiredCount: REQUIRED_BEGINNER_COUNT,
    });

    if (!hasRequiredBeginner) {
        return {
            eligible: false,
            reason: REJECTION_REASONS.MISSING_BEGINNER,
            context: {
                requiredCount: REQUIRED_BEGINNER_COUNT,
            },
        };
    }

    return { eligible: true };
};

module.exports = {
    hasIntermediateEligibility,
};
