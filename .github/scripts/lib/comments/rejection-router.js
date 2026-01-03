const { beginnerRejection } = require('./difficulty-02-beginner');
const { capacityLimitReached } = require('./max-assignments-reached');
const { spamNonGfiAssignment } = require('./spam-restrictions');

const REJECTION_REASONS =
    require('../eligibility/rejection-reasons');

const rejectionRouter = ({ reason, context, username, urls }) => {
    switch (reason) {
        case REJECTION_REASONS.MISSING_GFI:
            return beginnerRejection({
                username,
                completedGfiCount: context.completedGfiCount,
                browseGfiUrl: urls.gfi,
            });

        case REJECTION_REASONS.CAPACITY:
            return capacityLimitReached({
                username,
                openAssignedCount: context.openAssignedCount,
                maxAllowed: context.maxAllowed,
            });

        case REJECTION_REASONS.SPAM:
            return spamNonGfiAssignment(username);

        default:
            return null;
    }
};

module.exports = { rejectionRouter };
