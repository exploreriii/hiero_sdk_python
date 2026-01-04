const { hasAdvancedEligibility } =
    require('../lib/eligibility/has-eligibility-04-advanced');
const { rejectionRouter } =
    require('../lib/comments/rejection-router');

const ADVANCED_LABEL = 'Advanced';

function isAdvanced(issue) {
    return (issue.labels ?? []).some(l => l.name === ADVANCED_LABEL);
}

module.exports = async ({ github, context }) => {
    const { issue, assignee } = context.payload;
    const { owner, repo } = context.repo;

    if (!issue || !assignee) return;
    if (!isAdvanced(issue)) return;

    const username = assignee.login;

    console.log('[advanced-enforce] Checking eligibility', {
        issue: issue.number,
        username,
    });

    const result = await hasAdvancedEligibility({
        github,
        owner,
        repo,
        username,
    });

    if (result.eligible) {
        console.log('[advanced-enforce] Assignment allowed', {
            issue: issue.number,
            username,
        });
        return;
    }

    // ❌ Not eligible → revert assignment
    await github.rest.issues.removeAssignees({
        owner,
        repo,
        issue_number: issue.number,
        assignees: [username],
    });

    const body = rejectionRouter({
        reason: result.reason,
        context: result.context,
        username,
    });

    if (body) {
        await github.rest.issues.createComment({
            owner,
            repo,
            issue_number: issue.number,
            body,
        });
    }

    console.log('[advanced-enforce] Assignment reverted', {
        issue: issue.number,
        username,
        reason: result.reason,
    });
};
