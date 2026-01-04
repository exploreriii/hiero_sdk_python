const { beginnerRejection } = require('./difficulty-02-beginner');
const { intermediateRejection } = require('./difficulty-03-intermediate');
const { advancedRejection } = require('./difficulty-04-advanced');
const { capacityLimitReached } = require('./max-assignments-reached');
const { spamNonGfiAssignment } = require('./spam-restrictions');

const REJECTION_REASONS =
    require('../eligibility/rejection-reasons');

const rejectionRouter = ({ reason, context = {}, username, urls = {} }) => {
    switch (reason) {
        // ───── Beginner → Intermediate ladder
        case REJECTION_REASONS.MISSING_GFI:
        case REJECTION_REASONS.MISSING_BEGINNER:
            return intermediateRejection({
                username,
                requiredGfiCount: context.requiredGfiCount ?? 1,
                requiredBeginnerCount: context.requiredBeginnerCount ?? 1,
                browseGfiUrl: urls.gfi,
                browseBeginnerUrl: urls.beginner,
            });

        // ───── Intermediate → Advanced ladder
        case REJECTION_REASONS.MISSING_INTERMEDIATE:
            return advancedRejection({
                username,
                requiredIntermediateCount: context.requiredCount ?? 1,
                browseIntermediateUrl: urls.intermediate,
            });

        // ───── Shared rules
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
