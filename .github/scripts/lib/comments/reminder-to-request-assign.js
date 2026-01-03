const BOT_SIGNATURE = '\n\n— 🤖 Automated helper';

function assignReminder(username, tierName) {
    return `
<!-- assign-reminder -->
👋 Hi @${username}!

If you’d like to work on this **${tierName} issue**, just comment:

\`\`\`
/assign
\`\`\`

and I’ll take care of the rest 🤖${BOT_SIGNATURE}
`;
}

module.exports = {
    assignReminder,
};
