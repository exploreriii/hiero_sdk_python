//
// Auto-assigns a Beginner Issue when a human user comments "/assign".
// Requirement: user must have completed at least one Good First Issue.
// Assumes: other bots continue to enforce max 2 issues at a time, spam guards, etc.
// GFI completion logic is handled by reusable scripts/lib/has-gfi.js
//

const { hasCompletedGfi } = require('./lib/has-gfi');

const BEGINNER_ISSUE_LABEL = 'beginner';
const ASSIGN_REMINDER_MARKER = '<!-- Beginner assign reminder -->';

const UNASSIGNED_GFI_SEARCH_URL =
    'https://github.com/hiero-ledger/hiero-sdk-python/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22Good%20First%20Issue%22%20no%3Aassignee';
const UNASSIGNED_BEGINNER_SEARCH_URL =
    'https://github.com/hiero-ledger/hiero-sdk-python/issues?q=is%3Aissue%20state%3Aopen%20label%3Abeginner%20no%3Aassignee';

/// ─────────────────────────────────────────────────────────────
/// HELPERS – BASIC CHECKS
/// ─────────────────────────────────────────────────────────────

function commentRequestsAssignment(body) {
    const matches =
        typeof body === 'string' &&
        /(^|\s)\/assign(\s|$)/i.test(body);

    console.log('[beginner-assign] commentRequestsAssignment:', {
        body,
        matches,
    });

    return matches;
}

function issueIsBeginnerIssue(issue) {
    const labels = issue?.labels?.map(l => l.name) ?? [];
    const isBeginner = labels.includes(BEGINNER_ISSUE_LABEL);

    console.log('[beginner-assign] issueIsBeginnerIssue:', {
        labels,
        expected: BEGINNER_ISSUE_LABEL,
        isBeginner,
    });

    return isBeginner;
}

function getCurrentAssigneeMention(issue) {
    const login = issue?.assignees?.[0]?.login;
    return login ? `@${login}` : 'someone';
}

/// ─────────────────────────────────────────────────────────────
/// HELPERS – COMMENTS
/// ─────────────────────────────────────────────────────────────

function commentAlreadyAssigned(username, issue) {
    return (
        `Hi @${username} — thanks for your interest in this issue!

This one is already assigned to ${getCurrentAssigneeMention(issue)}, so I can’t assign it again right now.

👉 **Take a look at other open Beginner Issues to work on:**  
[Browse unassigned Beginner Issues](${UNASSIGNED_BEGINNER_SEARCH_URL})

Once you find one you like, just comment \`/assign\` to get started 😊`
    );
}

function buildAssignReminder(username) {
    return `${ASSIGN_REMINDER_MARKER}
👋 Hi @${username}!

If you’d like to work on this **Beginner Issue**, just comment:

\`\`\`
/assign
\`\`\`

and you’ll be automatically assigned.`;
}

function buildMissingGfiRequirementComment(username) {
    return (
        `Hi @${username}! 👋

Before working on **Beginner Issues**, we ask contributors to complete **at least one Good First Issue** first.

👉 **Start here:**  
[Browse unassigned Good First Issues](${UNASSIGNED_GFI_SEARCH_URL})

Once you’ve completed one, feel free to come back and request this issue if not assigned. 🚀`
    );
}

/// ─────────────────────────────────────────────────────────────
/// ENTRY POINT
/// ─────────────────────────────────────────────────────────────

module.exports = async ({ github, context }) => {
    try {
        const { issue, comment } = context.payload;
        const { owner, repo } = context.repo;

        console.log('[beginner-assign] Payload snapshot:', {
            issueNumber: issue?.number,
            commenter: comment?.user?.login,
            commenterType: comment?.user?.type,
            commentBody: comment?.body,
            assignees: issue?.assignees?.map(a => a.login),
        });

        // Basic validation
        if (!issue?.number) {
            console.log('[beginner-assign] Exit: missing issue number');
            return;
        }

        if (!comment?.body) {
            console.log('[beginner-assign] Exit: missing comment body');
            return;
        }

        if (!comment?.user?.login) {
            console.log('[beginner-assign] Exit: missing commenter login');
            return;
        }

        if (comment.user.type === 'Bot') {
            console.log('[beginner-assign] Exit: comment authored by bot');
            return;
        }

        // Gentle reminder if user comments without /assign
        if (!commentRequestsAssignment(comment.body)) {
            if (
                issueIsBeginnerIssue(issue) &&
                !issue.assignees?.length
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

                const reminderAlreadyPosted = comments.some(c =>
                    c.body?.includes(ASSIGN_REMINDER_MARKER)
                );

                console.log('[beginner-assign] Reminder check:', {
                    reminderAlreadyPosted,
                });

                if (!reminderAlreadyPosted) {
                    await github.rest.issues.createComment({
                        owner,
                        repo,
                        issue_number: issue.number,
                        body: buildAssignReminder(comment.user.login),
                    });

                    console.log('[beginner-assign] Posted /assign reminder');
                }
            }

            console.log('[beginner-assign] Exit: comment does not request assignment');
            return;
        }

        console.log('[beginner-assign] Assignment command detected');

        // Only act on Beginner Issues
        if (!issueIsBeginnerIssue(issue)) {
            console.log('[beginner-assign] Exit: issue is not Beginner Issue');
            return;
        }

        const requester = comment.user.login;

        console.log('[beginner-assign] Requester:', requester);

        // Already assigned
        if (issue.assignees?.length > 0) {
            console.log('[beginner-assign] Exit: issue already assigned');

            await github.rest.issues.createComment({
                owner,
                repo,
                issue_number: issue.number,
                body: commentAlreadyAssigned(requester, issue),
            });

            console.log('[beginner-assign] Posted already-assigned comment');
            return;
        }

        console.log('[beginner-assign] Checking GFI completion for user');

        // Enforce GFI prerequisite
        const hasGfi = await hasCompletedGfi({
            github,
            owner,
            repo,
            username: requester,
        });

        console.log('[beginner-assign] hasCompletedGfi result:', {
            requester,
            hasGfi,
        });

        if (!hasGfi) {
            await github.rest.issues.createComment({
                owner,
                repo,
                issue_number: issue.number,
                body: buildMissingGfiRequirementComment(requester),
            });

            console.log('[beginner-assign] Posted missing-GFI requirement comment');
            return;
        }

        console.log('[beginner-assign] Assigning issue to requester');

        // Assign issue
        await github.rest.issues.addAssignees({
            owner,
            repo,
            issue_number: issue.number,
            assignees: [requester],
        });

        console.log('[beginner-assign] Assignment completed successfully');
    } catch (error) {
        console.error('[beginner-assign] Error:', {
            message: error.message,
            status: error.status,
            issueNumber: context.payload.issue?.number,
            commenter: context.payload.comment?.user?.login,
        });
        throw error;
    }
};
