const { hasAdvancedEligibility } =
    require('../lib/eligibility/has-eligibility-04-advanced');
const { rejectionRouter } =
    require('../lib/comments/rejection-router');

const ADVANCED_LABEL = 'Advanced';

function isAdvanced(issue) {
    return (issue.labels ?? []).some(
        l => l.name?.toLowerCase() === ADVANCED_LABEL.toLowerCase()
    );
}

module.exports = async ({ github, context }) => {
    console.log('[advanced-enforce] Workflow triggered', {
        action: context.payload.action,
        issue: context.payload.issue?.number,
        assignee: context.payload.assignee?.login,
        labels: context.payload.issue?.labels?.map(l => l.name),
    });

    const { issue, assignee } = context.payload;
    const { owner, repo } = context.repo;

    if (!issue || !assignee) {
        console.log('[advanced-enforce] Exit: missing issue or assignee');
        return;
    }

    if (!isAdvanced(issue)) {
        console.log('[advanced-enforce] Exit: issue is not Advanced');
        return;
    }

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

    console.log('[advanced-enforce] Eligibility result', {
        issue: issue.number,
        username,
        eligible: result.eligible,
        reason: result.reason,
        context: result.context,
    });

    if (result.eligible) {
        console.log('[advanced-enforce] Assignment allowed', {
            issue: issue.number,
            username,
        });
        return;
    }

    // ❌ Not eligible → revert assignment
    console.log('[advanced-enforce] Reverting assignment', {
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
        console.log('[advanced-enforce] Posting rejection comment', {
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
        console.log('[advanced-enforce] No rejection message generated', {
            reason: result.reason,
        });
    }

    console.log('[advanced-enforce] Assignment reverted', {
        issue: issue.number,
        username,
        reason: result.reason,
    });
};
