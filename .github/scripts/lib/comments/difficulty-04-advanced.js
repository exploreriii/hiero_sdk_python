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
const advancedRejection = ({
  username,
  intermediateCount,
  suggestionLabel,
  suggestionUrl,
}) => `Hi @${username}, I can’t assign you to this issue just yet.

**Why?**  
Advanced issues involve higher-risk changes to core parts of the codebase. They typically require more extensive testing and may impact automation and CI behavior.

**Requirements:**  
- Completion of at least **2 intermediate issues**  
  (you have completed **${intermediateCount}**)

To build the required experience, please review our **[${suggestionLabel}](${suggestionUrl})** tasks. Once you’ve completed a few more, you’ll be eligible to work on advanced issues.`;

module.exports = {
  advancedRejection,
};
