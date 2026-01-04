const { isTeam } = require('../team/has-team');
const { isOnSpamList } = require('../counts/is-on-spam-list');
const { hasCompletedBeginner } = require('../counts/has-completed-n-02-beginner');
const { countOpenAssignedIssues } = require('../counts/count-opened-assigned-issues');
const REJECTION_REASONS = require('./rejection-reasons');

// Configurable
const MAX_OPEN_ASSIGNED_ISSUES = 2;
const REQUIRED_BEGINNER_COUNT = 1;

// Spam users are disabled for intermediate issues
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
