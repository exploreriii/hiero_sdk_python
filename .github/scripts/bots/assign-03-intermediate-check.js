const { hasIntermediateEligibility } = require('../lib/eligibility/has-eligibility-03-intermediate');
const { rejectionRouter } = require('../lib/comments/rejection-router');

const INTERMEDIATE_LABEL = 'Intermediate';

function isIntermediate(issue) {
    return (issue.labels ?? []).some(l => l.name === INTERMEDIATE_LABEL);
}

module.exports = async ({ github, context }) => {
    const { issue, assignee } = context.payload;
    const { owner, repo } = context.repo;

    if (!issue || !assignee) return;
    if (!isIntermediate(issue)) return;

    const username = assignee.login;

    const result = await hasIntermediateEligibility({
        github,
        owner,
        repo,
        username,
    });

    if (result.eligible) {
        console.log('[intermediate-enforce] Assignment allowed', {
            issue: issue.number,
            username,
        });
        return;
    }

    // ❌ Not eligible → unassign
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

    console.log('[intermediate-enforce] Assignment reverted', {
        issue: issue.number,
        username,
        reason: result.reason,
    });
};
