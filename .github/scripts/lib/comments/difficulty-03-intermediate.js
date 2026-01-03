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
const INTERMEDIATE_GUARD_MARKER = '<!-- Intermediate Issue Guard -->';

const intermediateRejection = ({
    username,
    completedGfiCount,
    hasBeginner,
    browseGfiUrl,
    browseBeginnerUrl,
}) => {
    const gfiPlural = completedGfiCount === 1 ? '' : 's';
    const reasons = [];

    if (completedGfiCount === 0) {
        reasons.push('• You have not completed a **Good First Issue** yet');
    }

    if (!hasBeginner) {
        reasons.push('• You have not completed a **Beginner issue** yet');
    }

    return `${INTERMEDIATE_GUARD_MARKER}
Hi @${username}, thank you for your interest in this issue.

This issue is labeled **Intermediate**, which means it requires some prior experience with the project.

**Why you can’t be assigned right now:**
${reasons.join('\n')}

**Your progress so far:**
- Completed **${completedGfiCount}** Good First Issue${gfiPlural}
- Beginner issue completed: **${hasBeginner ? 'Yes' : 'No'}**

**Suggested next steps:**
- [Browse unassigned Good First Issues](${browseGfiUrl})
- [Browse unassigned Beginner issues](${browseBeginnerUrl})

Once you meet the requirements, you’re welcome to come back and request this issue again.`;
};

module.exports = {
    intermediateRejection,
};
