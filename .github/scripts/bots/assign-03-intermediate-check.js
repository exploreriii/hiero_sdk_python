const { hasIntermediateEligibility } =
    require('../lib/eligibility/has-eligibility-03-intermediate');
const { rejectionRouter } =
    require('../lib/comments/rejection-router');

const INTERMEDIATE_LABEL = 'Intermediate';

function isIntermediate(issue) {
    return (issue.labels ?? []).some(
        l => l.name?.toLowerCase() === INTERMEDIATE_LABEL.toLowerCase()
    );
}

module.exports = async ({ github, context }) => {
    console.log('[intermediate-enforce] Workflow triggered', {
        action: context.payload.action,
        issue: context.payload.issue?.number,
        assignee: context.payload.assignee?.login,
        labels: context.payload.issue?.labels?.map(l => l.name),
    });

    const { issue, assignee } = context.payload;
    const { owner, repo } = context.repo;

    if (!issue || !assignee) {
        console.log('[intermediate-enforce] Exit: missing issue or assignee');
        return;
    }

    if (!isIntermediate(issue)) {
        console.log('[intermediate-enforce] Exit: issue is not Intermediate');
        return;
    }

    const username = assignee.login;

    console.log('[intermediate-enforce] Checking eligibility', {
        issue: issue.number,
        username,
    });

    const result = await hasIntermediateEligibility({
        github,
        owner,
        repo,
        username,
    });

    console.log('[intermediate-enforce] Eligibility result', {
        issue: issue.number,
        username,
        eligible: result.eligible,
        reason: result.reason,
        context: result.context,
    });

    if (result.eligible) {
        console.log('[intermediate-enforce] Assignment allowed', {
            issue: issue.number,
            username,
        });
        return;
    }

    // ❌ Not eligible → unassign
    console.log('[intermediate-enforce] Reverting assignment', {
        issue: issue.number,
        username,
    });

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
        console.log('[intermediate-enforce] Posting rejection comment', {
            issue: issue.number,
            username,
            reason: result.reason,
        });

        await github.rest.issues.createComment({
            owner,
            repo,
            issue_number: issue.number,
            body,
        });
    } else {
        console.log('[intermediate-enforce] No rejection message generated', {
            reason: result.reason,
        });
    }

    console.log('[intermediate-enforce] Assignment reverted', {
        issue: issue.number,
        username,
        reason: result.reason,
    });
};
