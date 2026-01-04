const { beginnerRejection } = require('./difficulty-02-beginner');
const { intermediateRejection } = require('./difficulty-03-intermediate');
const { advancedRejection } = require('./difficulty-04-advanced');
const { capacityLimitReached } = require('./max-assignments-reached');
const {
    spamNonGfiAssignment,
    spamAssignmentLimitExceeded,
} = require('./spam-restrictions');

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

        // ─────────────────────────────────────────
        // Capacity limits (branch on spam status)
        // ─────────────────────────────────────────
        case REJECTION_REASONS.CAPACITY:
            if (context.isSpamListed) {
                return spamAssignmentLimitExceeded(
                    username,
                    context.openAssignedCount
                );
            }

            return capacityLimitReached({
                username,
                openAssignedCount: context.openAssignedCount,
                maxAllowed: context.maxAllowed,
            });

        // ─────────────────────────────────────────
        // Spam attempting non-GFI assignment
        // ─────────────────────────────────────────
        case REJECTION_REASONS.SPAM:
            return spamNonGfiAssignment(username);

        default:
            return null;
    }
};

module.exports = { rejectionRouter };
