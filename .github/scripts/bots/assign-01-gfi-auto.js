/**
 * Auto-assigns a Good First Issue when a user comments `/assign`.
 *
 * Architecture:
 * - Policy lives in lib/eligibility/*
 * - Messaging lives in lib/comments/*
 * - This file only orchestrates
 */

const { isTeam } = require('../lib/team/has-team');
const { hasGfiEligibility } = require('../lib/eligibility/has-eligibility-01-gfi');
const { rejectionRouter } = require('../lib/comments/rejection-router');
const { assignReminder } = require('../lib/comments/reminder-to-request-assign');
const { alreadyAssigned } = require('../lib/comments/issue-already-assigned');
const assignMentor =
    require('./assign-01-gfi-mentor');

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

    // ─────────────────────────────────────────────
    // Guard rails & early exits
    // ─────────────────────────────────────────────
    if (!issue || !comment) {
        console.log('[gfi-assign] Exit: missing issue or comment');
        return;
    }

    if (comment.user?.type === 'Bot') {
        console.log('[gfi-assign] Exit: comment authored by bot');
        return;
    }

    if (!isGfiIssue(issue)) {
        console.log('[gfi-assign] Exit: issue is not Good First Issue', {
            labels: issue.labels?.map(l => l.name),
        });
        return;
    }

    const username = comment.user.login;

    console.log('[gfi-assign] Start', {
        issue: issue.number,
        username,
        commentBody: comment.body,
    });

    // ─────────────────────────────────────────────
    // Reminder flow (no /assign)
    // ─────────────────────────────────────────────
    if (!requestsAssignment(comment.body)) {
        console.log('[gfi-assign] No /assign detected, evaluating reminder');

        const isTeamMember = await isTeam({ github, owner, repo, username });

        console.log('[gfi-assign] Reminder eligibility', {
            isTeamMember,
            hasAssignee: !!issue.assignees?.length,
        });

        if (!issue.assignees?.length && !isTeamMember) {
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

            console.log('[gfi-assign] Reminder presence', {
                alreadyReminded,
            });

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

        console.log('[gfi-assign] Exit: reminder path complete');
        return;
    }

    console.log('[gfi-assign] /assign command detected');

    // ─────────────────────────────────────────────
    // Already assigned
    // ─────────────────────────────────────────────
    if (issue.assignees?.length) {
        console.log('[gfi-assign] Exit: issue already assigned', {
            assignee: issue.assignees[0]?.login,
        });

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

    console.log('[gfi-assign] Eligibility result', {
        username,
        result,
    });

    if (!result.eligible) {
        const body = rejectionRouter({
            reason: result.reason,
            context: result.context,
            username,
            urls: BROWSE_URLS,
        });

        console.log('[gfi-assign] Rejection routed', {
            reason: result.reason,
            hasBody: !!body,
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
    console.log('[gfi-assign] Assigning issue', {
        issue: issue.number,
        assignee: username,
    });

    await github.rest.issues.addAssignees({
        owner,
        repo,
        issue_number: issue.number,
        assignees: [username],
    });
    console.log('[gfi-assign] Triggering mentor assignment');

    await assignMentor({
        github,
        context: {
            repo: {
                owner,
                repo,
            },
            payload: {
                issue,
                assignee: {
                    login: username,
                    type: 'User',
                },
            },
        },
    });

    console.log('[gfi-assign] Assigned successfully', {
        issue: issue.number,
        username,
    });
};
