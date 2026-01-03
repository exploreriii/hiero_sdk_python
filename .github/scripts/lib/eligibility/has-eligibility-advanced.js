// Reusable function to check if a user is eligible for Advanced issues
//
// Eligibility requirements (for non-committers):
// - At least 2 completed Intermediate Issues
// - Fewer than 2 open assigned issues (across the SDK repo)
//
// RESTRICTIONS:
// - Users on the spam list are NOT eligible for Advanced issues.
//
// ADVANCED EXEMPTION RULE:
// - ONLY committers (write / maintain / admin) may bypass eligibility checks.
// - Triage members are NOT exempt and must still meet all requirements.
//
// NOTE FOR MAINTAINERS:
// - The "2 Intermediate issues" requirement is enforced inside
//   hasCompletedIntermediate().
// - Capacity limits are enforced consistently across tiers.
// - This helper is policy-only; enforcement lives in bots.

const { isCommitter } = require('./is-committer');
const { isOnSpamList } = require('../counts/is-on-spam-list');
const { hasCompletedIntermediate } = require('./has-intermediate');
const { countOpenAssignedIssues } = require('./count-open-assigned-issues');

const MAX_OPEN_ASSIGNED_ISSUES = 2;

async function hasAdvancedEligibility({ github, owner, repo, username }) {
    console.log('[has-advanced-eligibility] Start check:', {
        owner,
        repo,
        username,
    });

    // Committers bypass all Advanced eligibility checks
    if (await isCommitter({ github, owner, repo, username })) {
        console.log('[has-advanced-eligibility] Skipped: user is committer', {
            username,
        });
        return true;
    }

    // Spam-listed users are never eligible for Advanced issues
    if (await isOnSpamList({ github, owner, repo, username })) {
        console.log('[has-advanced-eligibility] Exit: user is on spam list', {
            username,
        });
        return false;
    }

    // Capacity check (max 2 open issues across the repo)
    const openAssignedCount = await countOpenAssignedIssues({
        github,
        owner,
        repo,
        username,
    });

    if (openAssignedCount >= MAX_OPEN_ASSIGNED_ISSUES) {
        console.log('[has-advanced-eligibility] Exit: assignment limit reached', {
            username,
            openAssignedCount,
        });
        return false;
    }

    // Intermediate requirement (>= 2, enforced in hasCompletedIntermediate)
    const hasRequiredIntermediate = await hasCompletedIntermediate({
        github,
        owner,
        repo,
        username,
    });

    if (!hasRequiredIntermediate) {
        console.log(
            '[has-advanced-eligibility] Exit: missing required Intermediate completions',
            { username }
        );
        return false;
    }

    console.log('[has-advanced-eligibility] Success: user is eligible for Advanced issues', {
        username,
    });

    return true;
}

module.exports = {
    hasAdvancedEligibility,
};
