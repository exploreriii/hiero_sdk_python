// Reusable function to check if a user is eligible for Beginner issues
//
// Eligibility requirements:
// - At least 1 completed Good First Issue
// - Fewer than 2 open assigned issues
//
// RESTRICTIONS:
// - Users on the spam list are NOT eligible for Beginner issues.
//
// EXEMPTION RULE:
// - Committers (write / maintain / admin) bypass all eligibility checks.
//
// NOTE FOR MAINTAINERS:
// - Beginner eligibility is intentionally minimal.
// - Capacity limits are enforced consistently across tiers.
// - Do NOT add additional requirements here unless the onboarding
//   ladder is explicitly changed.
//
// Bot behavior (comments, assignment, enforcement) must live elsewhere.

const { isCommitter } = require('./is-committer');
const { isOnSpamList } = require('../counts/is-on-spam-list');
const { hasCompletedGfi } = require('./has-gfi');
const { countOpenAssignedIssues } = require('./count-open-assigned-issues');

const MAX_OPEN_ASSIGNED_ISSUES = 2;

async function hasBeginnerEligibility({ github, owner, repo, username }) {
    console.log('[has-beginner-eligibility] Start check:', {
        owner,
        repo,
        username,
    });

    // Committers bypass all Beginner eligibility checks
    if (await isCommitter({ github, owner, repo, username })) {
        console.log('[has-beginner-eligibility] Skipped: user is committer', {
            username,
        });
        return true;
    }

    // Spam-listed users are never eligible for Beginner issues
    if (await isOnSpamList({ github, owner, repo, username })) {
        console.log('[has-beginner-eligibility] Exit: user is on spam list', {
            username,
        });
        return false;
    }

    // Capacity check (max 2 open issues)
    const openAssignedCount = await countOpenAssignedIssues({
        github,
        owner,
        repo,
        username,
    });

    if (openAssignedCount >= MAX_OPEN_ASSIGNED_ISSUES) {
        console.log('[has-beginner-eligibility] Exit: assignment limit reached', {
            username,
            openAssignedCount,
        });
        return false;
    }

    const hasGfi = await hasCompletedGfi({
        github,
        owner,
        repo,
        username,
    });

    if (!hasGfi) {
        console.log('[has-beginner-eligibility] Exit: missing GFI completion', {
            username,
        });
        return false;
    }

    console.log('[has-beginner-eligibility] Success: user is eligible for Beginner issues', {
        username,
    });

    return true;
}

module.exports = {
    hasBeginnerEligibility,
};
