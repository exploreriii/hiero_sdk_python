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
const beginnerRejection = ({
    username,
    completedGfiCount,
    browseGfiUrl,
}) => {
    const gfiPlural = completedGfiCount === 1 ? '' : 's';

    return `Hi @${username},

Thank you for your interest in contributing — we’re glad to see you here.

This issue is labeled **Beginner**, which is intended as the next step after completing a **Good First Issue**.

**Requirement:**  
- Completion of **one Good First Issue**

**Your progress:**  
- Completed **${completedGfiCount}** Good First Issue${gfiPlural}

You can find available tasks here:  
**[Browse unassigned Good First Issues](${browseGfiUrl})**

Once you’ve completed a GFI, feel free to come back and request this issue again.`;
};

module.exports = {
    beginnerRejection,
};
