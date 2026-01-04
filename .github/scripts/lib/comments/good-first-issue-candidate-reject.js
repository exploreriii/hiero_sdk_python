const gfiCandidateNotReady = ({ username, browseGfiUrl }) => {
    return `
<!-- gfi-candidate-not-ready -->

🚫 **This issue is not ready to be assigned yet**

@${username}, this issue is currently marked as a **Good First Issue Candidate**.

It is waiting for a maintainer to review and confirm that it is suitable as a **Good First Issue**.

### ✅ What you can do now
You can browse and pick from available **Good First Issues** that are ready to be assigned:
👉 ${browseGfiUrl}

Thank you for your interest and patience 🙏
`.trim();
};

module.exports = { gfiCandidateNotReady };
