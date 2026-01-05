/**
 * Generates a rejection message when a contributor lacks the
 * required experience to be assigned an advanced issue.
 *
 * This helper is informational only and does not perform any
 * assignment or eligibility logic.
 *
 * @param {Object} params
 * @param {string} params.username - GitHub username of the contributor
 * @param {number} params.intermediateCount - Number of completed intermediate issues
 * @param {string} params.suggestionLabel - Label for suggested issues - pass advanced
 * @param {string} params.suggestionUrl - URL to suggested issues - pass advanced URL
 * @returns {string} Formatted markdown message explaining the restriction
 */
const {
  ISSUE_TYPES,
  ELIGIBILITY_REQUIREMENTS,
} = require('../eligibility/requirements');

const advancedRejection = ({
  username,
  completedIntermediateCount,
  suggestionLabel,
  suggestionUrl,
}) => {
  const req =
    ELIGIBILITY_REQUIREMENTS[ISSUE_TYPES.ADVANCED];

  const intermediateReq =
    req.prerequisites.find(p => p.type === 'intermediate');

  const requiredCount = intermediateReq.requiredCount;
  const met = completedIntermediateCount >= requiredCount;

  return `Hi @${username}, I can’t assign you to this issue just yet.

**Why?**  
Advanced issues involve higher-risk changes to core parts of the codebase. They typically require more extensive testing and may impact automation and CI behavior.

**Requirements:**  
- Completion of **${requiredCount} Intermediate issue${requiredCount === 1 ? '' : 's'}**

**Your progress:**  
- Intermediate issues completed: **${completedIntermediateCount} / ${requiredCount}** ${met ? '✅' : '❌'}

To build the required experience, please review our **[${suggestionLabel}](${suggestionUrl})** tasks. Once the requirement is met, you’ll be eligible to work on advanced issues.`;
};

module.exports = {
  advancedRejection,
};