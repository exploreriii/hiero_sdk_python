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
    const { issue, comment } = context.payload;
    const { owner, repo } = context.repo;

    if (!issue || !comment) return;
    if (comment.user?.type === 'Bot') return;
    if (!requestsAssignment(comment.body)) return;
    if (!isGfiCandidate(issue)) return;

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

    if (alreadyPosted) return;

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
