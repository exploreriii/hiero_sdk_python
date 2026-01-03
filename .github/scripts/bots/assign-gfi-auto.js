/**
 * Auto-assigns a Good First Issue when a user comments `/assign`.
 *
 * Architecture:
 * - Policy lives in lib/eligibility/*
 * - Messaging lives in lib/comments/*
 * - This file only orchestrates
 */

const { isTeam } =
    require('../lib/team/has-team');

const { hasGfiEligibility } =
    require('../lib/eligibility/has-eligibility-01-gfi');

const { rejectionRouter } =
    require('../lib/comments/rejection-router');

const { assignReminder } =
    require('../lib/comments/reminder-to-request-assign');

const { alreadyAssigned } =
    require('../lib/comments/issue-already-assigned');

const GOOD_FIRST_ISSUE_LABEL = 'Good First Issue';
const ASSIGN_REMINDER_MARKER = '<!-- GFI assign reminder -->';

const BROWSE_URLS = {
    gfi: 'https://github.com/hiero-ledger/hiero-sdk-python/issues?q=is%3Aissue+state%3Aopen+label%3A"Good+First+Issue"+no%3Aassignee',
};

function requestsAssignment(body) {
    return typeof body === 'string' && /(^|\s)\/assign(\s|$)/i.test(body);
}

function isGfiIssue(issue) {
    return (issue.labels ?? []).some(l => l.name === GOOD_FIRST_ISSUE_LABEL);
}

module.exports = async ({ github, context }) => {
    const { issue, comment } = context.payload;
    const { owner, repo } = context.repo;

    if (!issue || !comment) return;
    if (comment.user?.type === 'Bot') return;
    if (!isGfiIssue(issue)) return;

    const username = comment.user.login;

    console.log('[gfi-assign] Start', {
        issue: issue.number,
        username,
    });

    // ─────────────────────────────────────────────
    // Gentle reminder if user comments but not /assign
    // (exclude team members)
    // ─────────────────────────────────────────────
    if (!requestsAssignment(comment.body)) {
        if (
            !issue.assignees?.length &&
            !(await isTeam({ github, owner, repo, username }))
        ) {
            const comments = await github.paginate(
                github.rest.issues.listComments,
                {
                    owner,
                    repo,
                    issue_number: issue.number,
                    per_page: 100,
                }
            );

            const alreadyReminded = comments.some(c =>
                c.body?.includes(ASSIGN_REMINDER_MARKER)
            );

            if (!alreadyReminded) {
                await github.rest.issues.createComment({
                    owner,
                    repo,
                    issue_number: issue.number,
                    body:
                        ASSIGN_REMINDER_MARKER +
                        assignReminder(username, 'Good First'),
                });

                console.log('[gfi-assign] Posted assign reminder');
            }
        }

        return;
    }

    // ─────────────────────────────────────────────
    // Already assigned
    // ─────────────────────────────────────────────
    if (issue.assignees?.length) {
        await github.rest.issues.createComment({
            owner,
            repo,
            issue_number: issue.number,
            body: alreadyAssigned({
                username,
                assignee: `@${issue.assignees[0].login}`,
                browseUrl: BROWSE_URLS.gfi,
                tierLabel: 'Good First',
            }),
        });
        return;
    }

    // ─────────────────────────────────────────────
    // Eligibility check (POLICY)
    // ─────────────────────────────────────────────
    const result = await hasGfiEligibility({
        github,
        owner,
        repo,
        username,
    });

    if (!result.eligible) {
        const body = rejectionRouter({
            reason: result.reason,
            context: result.context,
            username,
            urls: BROWSE_URLS,
        });

        if (body) {
            await github.rest.issues.createComment({
                owner,
                repo,
                issue_number: issue.number,
                body,
            });
        }

        return;
    }

    // ─────────────────────────────────────────────
    // Assign issue
    // ─────────────────────────────────────────────
    await github.rest.issues.addAssignees({
        owner,
        repo,
        issue_number: issue.number,
        assignees: [username],
    });

    console.log('[gfi-assign] Assigned successfully', {
        issue: issue.number,
        username,
    });
};
