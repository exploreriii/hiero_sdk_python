const { gfiCandidateNotReady } =
    require('../lib/comments/good-first-issue-candidate-reject');

const GFI_CANDIDATE_LABEL = 'Good First Issue Candidate';

const BROWSE_URLS = {
    gfi:
        'https://github.com/hiero-ledger/hiero-sdk-python/issues' +
        '?q=is%3Aissue+state%3Aopen+label%3A"Good+First+Issue"+no%3Aassignee',
};

function requestsAssignment(body) {
    return typeof body === 'string' && /(^|\s)\/assign(\s|$)/i.test(body);
}

function isGfiCandidate(issue) {
    return (issue.labels ?? []).some(
        l => l.name?.toLowerCase() === GFI_CANDIDATE_LABEL.toLowerCase()
    );
}

module.exports = async ({ github, context }) => {
    console.log('[gfi-candidate-guard] Workflow triggered', {
        issue: context.payload.issue?.number,
        commenter: context.payload.comment?.user?.login,
        labels: context.payload.issue?.labels?.map(l => l.name),
        body: context.payload.comment?.body,
    });

    const { issue, comment } = context.payload;
    const { owner, repo } = context.repo;

    if (!issue || !comment) {
        console.log('[gfi-candidate-guard] Exit: missing issue or comment');
        return;
    }

    if (comment.user?.type === 'Bot') {
        console.log('[gfi-candidate-guard] Exit: bot comment');
        return;
    }

    if (!requestsAssignment(comment.body)) {
        console.log('[gfi-candidate-guard] Exit: no /assign command');
        return;
    }

    if (!isGfiCandidate(issue)) {
        console.log('[gfi-candidate-guard] Exit: issue is not GFI candidate');
        return;
    }

    console.log('[gfi-candidate-guard] GFI candidate assignment attempted', {
        issue: issue.number,
        username: comment.user.login,
    });

    // Prevent duplicate comments
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
        console.log('[gfi-candidate-guard] Exit: rejection already posted', {
            issue: issue.number,
        });
        return;
    }

    console.log('[gfi-candidate-guard] Posting rejection comment', {
        issue: issue.number,
        username: comment.user.login,
    });

    await github.rest.issues.createComment({
        owner,
        repo,
        issue_number: issue.number,
        body: gfiCandidateNotReady({
            username: comment.user.login,
            browseGfiUrl: BROWSE_URLS.gfi,
        }),
    });

    console.log('[gfi-candidate-guard] Redirected user to available GFIs', {
        issue: issue.number,
        username: comment.user.login,
    });
};
