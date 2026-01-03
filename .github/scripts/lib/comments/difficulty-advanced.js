// Advanced issue guard messages
//
// Used when a user is removed from an Advanced issue due to
// insufficient prerequisite experience.

function advancedRejection({
    username,
    gfiCount,
    intermediateCount,
    suggestionLabel,
    suggestionUrl,
}) {
    return `Hi @${username}, I cannot assign you to this issue yet.

**Why?**
Advanced issues involve high-risk changes to the core codebase. They require significant testing and can impact automation and CI behavior.

**Requirement:**
- Complete at least **3** 'intermediate' issue (You have: **${intermediateCount}**)

Please check out our **[${suggestionLabel}](${suggestionUrl})** tasks to build your experience first!`;
}

module.exports = {
    advancedRejection,
};
