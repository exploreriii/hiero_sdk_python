/**
 * Automatically assigns a mentor when a human contributor
 * is assigned to a Good First Issue.
 *
 * Triggered by: issues.assigned
 *
 * Architecture:
 * - Comment text lives in lib/comments/assign-mentor-gfi.js
 * - All logic, API calls, and guards live here
 */

const fs = require('fs');
const path = require('path');

const { buildMentorComment, COMMENT_MARKER } =
    require('../lib/comments/assign-mentor-gfi');

// Defaults (can be overridden via env)
const MENTOR_TEAM_ALIAS =
    process.env.MENTOR_TEAM_ALIAS ||
    '@hiero-ledger/hiero-sdk-python-triage';

const SUPPORT_TEAM_ALIAS =
    process.env.SUPPORT_TEAM_ALIAS ||
    '@hiero-ledger/hiero-sdk-good-first-issue-support';

const DEFAULT_ROSTER_FILE = '.github/mentor_roster.json';
const GOOD_FIRST_ISSUE_LABEL = 'good first issue';

// ─────────────────────────────────────────────
// Helper: label guard
// ─────────────────────────────────────────────
function hasGoodFirstIssueLabel(issue) {
    return (issue.labels ?? []).some(label => {
        const name =
            typeof label === 'string'
                ? label
                : label?.name;

        return (
            typeof name === 'string' &&
            name.toLowerCase() === GOOD_FIRST_ISSUE_LABEL
        );
    });
}

// ─────────────────────────────────────────────
// Helper: load mentor roster
// ─────────────────────────────────────────────
function loadMentorRoster() {
    const rosterPath = path.resolve(
        process.cwd(),
        process.env.MENTOR_ROSTER_PATH || DEFAULT_ROSTER_FILE
    );

    console.log('[mentor-assign] Loading mentor roster:', rosterPath);

    const raw = fs.readFileSync(rosterPath, 'utf8');
    const parsed = JSON.parse(raw);

    const roster = (parsed.order ?? [])
        .map(entry => String(entry).trim())
        .filter(Boolean);

    if (!roster.length) {
        throw new Error('Mentor roster is empty');
    }

    return roster;
}

// ─────────────────────────────────────────────
// Helper: deterministic mentor selection
// ─────────────────────────────────────────────
function selectMentor(roster) {
    const dayIndex = Math.floor(
        Date.now() / (24 * 60 * 60 * 1000)
    );

    return roster[dayIndex % roster.length];
}

// ─────────────────────────────────────────────
// Entry point
// ─────────────────────────────────────────────
module.exports = async ({ github, context }) => {
    try {
        const { issue, assignee } = context.payload;

        // ─────────────────────────────────────────
        // Guard rails
        // ─────────────────────────────────────────
        if (!issue || !assignee) {
            console.log('[mentor-assign] Exit: missing issue or assignee');
            return;
        }

        if (assignee.type === 'Bot') {
            console.log('[mentor-assign] Exit: assignee is a bot', {
                assignee: assignee.login,
            });
            return;
        }

        if (!hasGoodFirstIssueLabel(issue)) {
            console.log('[mentor-assign] Exit: not a Good First Issue', {
                issue: issue.number,
            });
            return;
        }

        const { owner, repo } = context.repo;
        const mentee = assignee.login;

        console.log('[mentor-assign] Start', {
            issue: issue.number,
            mentee,
        });

        // ─────────────────────────────────────────
        // Prevent duplicate mentor comments
        // ─────────────────────────────────────────
        const comments = await github.paginate(
            github.rest.issues.listComments,
            {
                owner,
                repo,
                issue_number: issue.number,
                per_page: 100,
            }
        );

        const alreadyAssigned = comments.some(comment =>
            comment.body?.includes(COMMENT_MARKER)
        );

        console.log('[mentor-assign] Existing mentor comment check', {
            alreadyAssigned,
        });

        if (alreadyAssigned) {
            console.log('[mentor-assign] Exit: mentor already assigned');
            return;
        }

        // ─────────────────────────────────────────
        // Select mentor
        // ─────────────────────────────────────────
        const roster = loadMentorRoster();
        const mentor = selectMentor(roster);

        console.log('[mentor-assign] Mentor selected', {
            mentor,
        });

        // ─────────────────────────────────────────
        // Build & post comment (from lib)
        // ─────────────────────────────────────────
        const body = buildMentorComment({
            mentee,
            mentor,
            owner,
            repo,
            mentorTeamAlias: MENTOR_TEAM_ALIAS,
            supportTeamAlias: SUPPORT_TEAM_ALIAS,
        });

        await github.rest.issues.createComment({
            owner,
            repo,
            issue_number: issue.number,
            body,
        });

        console.log('[mentor-assign] Mentor comment posted successfully', {
            issue: issue.number,
            mentor,
            mentee,
        });
    } catch (error) {
        console.error('[mentor-assign] Failure', {
            message: error.message,
        });
        throw error;
    }
};
