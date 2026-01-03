/**
 * Generates a message when an issue cannot be assigned because it
 * already has an assignee.
 *
 * This helper is informational only and does not perform any
 * assignment or eligibility logic.
 *
 * @param {Object} params
 * @param {string} params.username - GitHub username of the requester
 * @param {string} params.assignee - Current assignee of the issue
 * @param {string} params.browseUrl - URL to browse unassigned issues
 * @param {string} params.tierLabel - Issue tier label (e.g. Beginner, Intermediate)
 * @returns {string} Formatted markdown message explaining the status
 */
const alreadyAssigned = ({
    username,
    assignee,
    browseUrl,
    tierLabel,
}) => `Hi @${username}, thank you for your interest in this issue.

This issue is currently assigned to **${assignee}**, so it can’t be assigned again at the moment.

You can browse other unassigned **${tierLabel}** issues here:  
**[View unassigned ${tierLabel} issues](${browseUrl})**

If you find an issue you’d like to work on, feel free to comment \`/assign\` and we’ll take it from there.`;

module.exports = {
    alreadyAssigned,
};
