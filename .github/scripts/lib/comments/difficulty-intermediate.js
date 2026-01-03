// Intermediate issue guard messages
//
// Used when a user is removed from an Intermediate issue because
// they do not meet the experience requirements.
//
// IMPORTANT:
// - Capacity limits are handled separately.
// - This message must stay in sync with hasIntermediateEligibility().
// - Do NOT add logic here — bots decide when to use this.

const INTERMEDIATE_GUARD_MARKER =
    process.env.INTERMEDIATE_COMMENT_MARKER || '<!-- Intermediate Issue Guard -->';

function intermediateRejection({
    username,
    completedGfiCount,
    hasBeginner,
    browseGfiUrl,
    browseBeginnerUrl,
}) {
    const gfiPlural = completedGfiCount === 1 ? '' : 's';

    let reasons = [];

    if (completedGfiCount === 0) {
        reasons.push(
            `• You haven’t completed a **Good First Issue** yet`
        );
    }

    if (!hasBeginner) {
        reasons.push(
            `• You haven’t completed a **Beginner issue** yet`
        );
    }

    return `${INTERMEDIATE_GUARD_MARKER}
Hi @${username}! Thanks for your interest in contributing 💡

This issue is labeled as **Intermediate**, which means it requires prior experience with the SDK.

**Why you can’t be assigned right now:**
${reasons.join('\n')}

**Your progress so far:**
- Completed **${completedGfiCount}** Good First Issue${gfiPlural}
- Beginner issue completed: **${hasBeginner ? 'Yes ✅' : 'No ❌'}**

👉 **Suggested next steps:**
- [Browse unassigned Good First Issues](${browseGfiUrl})
- [Browse unassigned Beginner issues](${browseBeginnerUrl})

Once you meet the requirements, feel free to come back and request this issue again — we’ll be happy to help 🚀`;
}

module.exports = {
    intermediateRejection,
};
