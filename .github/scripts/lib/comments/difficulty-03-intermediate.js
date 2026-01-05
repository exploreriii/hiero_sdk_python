/**
 * Generates a rejection message when a contributor does not yet
 * meet the requirements to be assigned an intermediate issue.
 *
 * This helper is informational only and does not perform any
 * assignment or eligibility logic.
 *
 * @param {Object} params
 * @param {string} params.username - GitHub username of the contributor
 * @param {number} params.completedGfiCount - Number of completed Good First Issues
 * @param {boolean} params.hasBeginner - Whether a Beginner issue has been completed
 * @param {string} params.browseGfiUrl - URL to browse Good First Issues
 * @param {string} params.browseBeginnerUrl - URL to browse Beginner issues
 * @returns {string} Formatted markdown message explaining the restriction
 */
const {
    ISSUE_TYPES,
    ELIGIBILITY_REQUIREMENTS,
} = require('../eligibility/requirements');

const INTERMEDIATE_GUARD_MARKER = '<!-- Intermediate Issue Guard -->';

const intermediateRejection = ({
    username,
    completedBeginnerCount,
    browseBeginnerUrl,
}) => {
    const req =
        ELIGIBILITY_REQUIREMENTS[ISSUE_TYPES.INTERMEDIATE];

    const beginnerReq =
        req.prerequisites.find(p => p.type === 'beginner');

    const requiredCount = beginnerReq.requiredCount;
    const met = completedBeginnerCount >= requiredCount;

    return `${INTERMEDIATE_GUARD_MARKER}
Hi @${username}, thank you for your interest in this issue.

This issue is labeled **Intermediate**, which requires prior experience working on **Beginner issues**.

**Requirements:**  
- Completion of **${requiredCount} Beginner issue${requiredCount === 1 ? '' : 's'}**

**Your progress:**  
- Beginner issues completed: **${completedBeginnerCount} / ${requiredCount}** ${met ? '✅' : '❌'}

**Suggested next steps:**  
- [Browse unassigned Beginner issues](${browseBeginnerUrl})

Once the requirement is met, you’re welcome to come back and request this issue again.`;
};

module.exports = {
    intermediateRejection,
};
