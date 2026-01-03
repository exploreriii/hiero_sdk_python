/**
 * Generates a reminder message explaining how to request assignment
 * to an issue.
 *
 * This helper is informational only and does not perform any
 * assignment or eligibility logic.
 *
 * @param {string} username - GitHub username of the contributor
 * @param {string} tierName - Issue tier name (e.g. Beginner, Intermediate)
 * @returns {string} Formatted markdown reminder message
 */
const BOT_SIGNATURE = '\n\n— Automated helper';

const assignReminder = (username, tierName) => `
Hi @${username},

If you’d like to work on this **${tierName} issue**, please comment:

\`\`\`
/assign
\`\`\`

and the bot will handle the assignment process.${BOT_SIGNATURE}
`;

module.exports = {
    assignReminder,
};

