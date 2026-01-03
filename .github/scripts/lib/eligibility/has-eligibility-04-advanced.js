const { isCommitter } =
    require('../team/has-team-committer-maintainer');
const { isOnSpamList } =
    require('../counts/is-on-spam-list');
const { hasCompletedIntermediate } =
    require('../counts/has-completed-n-03-intermediate');
const { countOpenAssignedIssues } =
    require('../counts/count-open-assigned-issues');
const REJECTION_REASONS =
    require('./rejection-reasons');

const MAX_OPEN_ASSIGNED_ISSUES = 2;
const REQUIRED_INTERMEDIATE_COUNT = 2;

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

    // Committers bypass all checks
    if (await isCommitter({ github, owner, repo, username })) {
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

    // Intermediate completion requirement
    const hasRequiredIntermediate =
        await hasCompletedIntermediate({
            github,
            owner,
            repo,
            username,
            requiredCount: REQUIRED_INTERMEDIATE_COUNT,
        });

    if (!hasRequiredIntermediate) {
        return {
            eligible: false,
            reason: REJECTION_REASONS.MISSING_INTERMEDIATE,
            context: {
                requiredCount: REQUIRED_INTERMEDIATE_COUNT,
            },
        };
    }

    return { eligible: true };
};

module.exports = {
    hasAdvancedEligibility,
};
