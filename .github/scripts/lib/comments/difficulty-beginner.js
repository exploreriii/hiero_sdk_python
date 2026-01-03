// Beginner issue guard messages
//
// Used when a user is removed from a Beginner issue because
// they have not yet completed the required experience.
//
// IMPORTANT:
// - Capacity limits are handled separately.
// - This message must stay in sync with hasBeginnerEligibility().
// - Do NOT add logic here — bots decide when to use this.

function beginnerRejection({
    username,
    completedGfiCount,
    browseGfiUrl,
}) {
    const gfiPlural = completedGfiCount === 1 ? '' : 's';

    return `Hi @${username}! 👋

Thanks so much for your interest in contributing — it’s great to see you here! 😊

This issue is labeled as **Beginner**, which is designed as the next step after completing a **Good First Issue**.

**What’s needed to move forward:**
- Complete **one Good First Issue**

**Your progress so far:**
- Completed **${completedGfiCount}** Good First Issue${gfiPlural}

👉 **A great place to start:**  
[Browse unassigned Good First Issues](${browseGfiUrl})

Once you’ve completed a GFI, you’re more than welcome to come back and request this issue again — we’ll be happy to help you take the next step 🚀`;
}

module.exports = {
    beginnerRejection,
};
