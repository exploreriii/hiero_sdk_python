/**
 * Generates a message when a contributor has reached the maximum
 * number of open issue assignments allowed.
 *
 * This helper is informational only and does not perform any
 * assignment or eligibility logic.
 *
 * @param {Object} params
 * @param {string} params.username - GitHub username of the contributor
 * @param {number} params.openAssignedCount - Number of currently assigned open issues
 * @param {number} params.maxAllowed - Maximum number of allowed open issues
 * @returns {string} Formatted markdown message explaining the limit
 */
const capacityLimitReached = ({
    username,
    openAssignedCount,
    maxAllowed,
}) => `Hi @${username}, thank you for your interest.

You currently have **${openAssignedCount} open issue${openAssignedCount === 1 ? '' : 's'}** assigned.

To keep assignments manageable, contributors may have at most **${maxAllowed} open issues** assigned at one time.

Once you complete or unassign one of your current issues, you’re welcome to request another.`;

module.exports = {
    capacityLimitReached,
};
