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
        // ─────────────────────────────────────────
        // Beginner eligibility failures
        // ─────────────────────────────────────────
        case REJECTION_REASONS.MISSING_GFI:
            return beginnerRejection({
                username,
                completedGfiCount: context.completedGfiCount ?? 0,
                browseGfiUrl: urls.gfi,
            });

        // ─────────────────────────────────────────
        // Intermediate eligibility failures
        // ─────────────────────────────────────────
        case REJECTION_REASONS.MISSING_BEGINNER:
            return intermediateRejection({
                username,
                completedBeginnerCount:
                    context.completedBeginnerCount ?? 0,
                requiredBeginnerCount:
                    context.requiredBeginnerCount ?? 1,
                browseBeginnerUrl: urls.beginner,
            });

        // ─────────────────────────────────────────
        // Advanced eligibility failures
        // ─────────────────────────────────────────
        case REJECTION_REASONS.MISSING_INTERMEDIATE:
            return advancedRejection({
                username,
                completedIntermediateCount:
                    context.completedIntermediateCount ?? 0,
                requiredIntermediateCount:
                    context.requiredIntermediateCount ?? 1,
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
        // Spam attempting disallowed assignment
        // ─────────────────────────────────────────
        case REJECTION_REASONS.SPAM:
            return spamNonGfiAssignment(username);

        default:
            return null;
    }
};

module.exports = { rejectionRouter };
