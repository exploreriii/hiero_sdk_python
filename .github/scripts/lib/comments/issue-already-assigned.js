function alreadyAssigned({ username, assignee, browseUrl, tierLabel }) {
    return `Hi @${username}! 👋

Thanks so much for your interest in this issue - we look forward to your contributions! 😊

This issue is currently assigned to ${assignee}, so I can’t assign it again right now.

👉 **Browse open ${tierLabel} issues that are still unassigned:**  
[View unassigned ${tierLabel} issues](${browseUrl})

If you find one you’d like to work on, just comment \`/assign\` and I’ll take care of the rest 🤖`;
}

