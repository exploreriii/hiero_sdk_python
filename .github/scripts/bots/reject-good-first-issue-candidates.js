const { gfiCandidateNotReady } =
    require('../lib/comments/good-first-issue-candidate-reject');

const GFI_CANDIDATE_LABEL = 'Good First Issue Candidate';

const BROWSE_URLS = {
    gfi:
        'https://github.com/hiero-ledger/hiero-sdk-python/issues' +
        '?q=is%3Aissue+state%3Aopen+label%3A"Good+First+Issue"+no%3Aassignee',
};

function isGfiCandidate(issue) {
    return (issue.labels ?? []).some(
        l => l.name?.toLowerCase() === GFI_CANDIDATE_LABEL.toLowerCase()
    );
}

module.exports = async ({ github, context }) => {
    const { issue, assignee, sender } = context.payload;
    const { owner, repo } = context.repo;

    console.log('[gfi-candidate-guard] Workflow triggered', {
        issue: issue?.number,
        assignee: assignee?.login,
        assignedBy: sender?.login,
        labels: issue?.labels?.map(l => l.name),
    });

    if (!issue || !assignee) {
        console.log('[gfi-candidate-guard] Exit: missing issue or assignee');
        return;
    }

    if (sender?.type === 'Bot') {
        console.log('[gfi-candidate-guard] Exit: bot actor');
        return;
    }

    if (!isGfiCandidate(issue)) {
        console.log('[gfi-candidate-guard] Exit: issue is not GFI candidate');
        return;
    }

    console.log('[gfi-candidate-guard] Invalid assignment detected', {
        issue: issue.number,
        assignee: assignee.login,
        assignedBy: sender.login,
    });

    // 🚨 ENFORCEMENT: remove the assignee
    await github.rest.issues.removeAssignees({
        owner,
        repo,
        issue_number: issue.number,
        assignees: [assignee.login],
    });

    // Prevent duplicate rejection comments
    const comments = await github.paginate(
        github.rest.issues.listComments,
        {
            owner,
            repo,
            issue_number: issue.number,
            per_page: 100,
        }
    );

    const alreadyPosted = comments.some(c =>
        c.body?.includes('<!-- gfi-candidate-not-ready -->')
    );

    if (alreadyPosted) {
        console.log('[gfi-candidate-guard] Exit: rejection already posted');
        return;
    }

    console.log('[gfi-candidate-guard] Posting rejection comment', {
        issue: issue.number,
        username: assignee.login,
    });

    await github.rest.issues.createComment({
        owner,
        repo,
        issue_number: issue.number,
        body: gfiCandidateNotReady({
            username: assignee.login,
            browseGfiUrl: BROWSE_URLS.gfi,
        }),
    });

    console.log('[gfi-candidate-guard] Assignment reverted and user notified', {
        issue: issue.number,
        username: assignee.login,
    });
};
