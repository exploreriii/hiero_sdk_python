/**
 * Generates a rejection message when a contributor is not yet
 * eligible to be assigned a beginner issue.
 *
 * This helper is informational only and does not perform any
 * assignment or eligibility logic.
 *
 *
 * @param {Object} params
 * @param {string} params.username - GitHub username of the contributor
 * @param {number} params.completedGfiCount - Number of completed Good First Issues
 * @param {string} params.browseGfiUrl - URL to browse available Good First Issues
 * @returns {string} Formatted markdown message explaining the restriction
 */
const {
    ISSUE_TYPES,
    ELIGIBILITY_REQUIREMENTS,
} = require('../eligibility/requirements');

const beginnerRejection = ({
    username,
    completedGfiCount,
    browseGfiUrl,
}) => {
    const req =
        ELIGIBILITY_REQUIREMENTS[ISSUE_TYPES.BEGINNER];

    const gfiRequirement =
        req.prerequisites.find(p => p.type === 'gfi');

    const requiredCount = gfiRequirement.requiredCount;
    const met = completedGfiCount >= requiredCount;

    return `Hi @${username},

Thank you for your interest in contributing — we’re glad to see you here.

This issue is labeled **Beginner**, which is intended as the next step after completing **Good First Issues (GFIs)**.

**Requirements:**  
- Completion of **${requiredCount} Good First Issue${requiredCount === 1 ? '' : 's'}**

**Your progress:**  
- Good First Issues completed: **${completedGfiCount} / ${requiredCount}** ${met ? '✅' : '❌'}

To build the required experience, please work on a GFI first:

**[Browse unassigned Good First Issues](${browseGfiUrl})**

Once the requirement is met, feel free to come back and request this issue again.`;
};

module.exports = {
    beginnerRejection,
};
