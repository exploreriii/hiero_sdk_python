// Tier eligibility helper: Intermediate issues
//
// Eligibility requirements (for non-triage users):
// - At least 1 completed Good First Issue
// - At least 1 completed Beginner Issue
// - Fewer than 2 open assigned issues (across the SDK repo)
//
// RESTRICTIONS:
// - Users on the spam list are NOT eligible for Intermediate issues.
//
// EXEMPTION RULE:
// - Triage members and above (triage / write / maintain / admin)
//   bypass eligibility checks and capacity limits.
//
// This helper is policy-only.
// Bots handle enforcement and UX.

const { isTriager } = require('./is-triager');
const { isOnSpamList } = require('../counts/is-on-spam-list');
const { hasCompletedGfi } = require('./has-gfi');
const { hasCompletedBeginner } = require('./has-beginner');
const { countOpenAssignedIssues } = require('./count-open-assigned-issues');

const MAX_OPEN_ASSIGNED_ISSUES = 2;

async function hasIntermediateEligibility({ github, owner, repo, username }) {
    console.log('[tiers] Checking Intermediate eligibility:', {
        owner,
        repo,
        username,
    });

    // Spam-listed users are never eligible
    if (await isOnSpamList({ github, owner, repo, username })) {
        console.log('[tiers] Exit: user is on spam list', {
            username,
        });
        return false;
    }

    // Triage members and above bypass Intermediate eligibility checks
    if (await isTriager({ github, owner, repo, username })) {
        console.log('[tiers] Skipped: user is triage+', {
            username,
        });
        return true;
    }

    // Capacity check (max 2 open issues across the repo)
    const openAssignedCount = await countOpenAssignedIssues({
        github,
        owner,
        repo,
        username,
    });

    if (openAssignedCount >= MAX_OPEN_ASSIGNED_ISSUES) {
        console.log('[tiers] Exit: assignment limit reached', {
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
        console.log('[tiers] Exit: missing GFI completion', {
            username,
        });
        return false;
    }

    const hasBeginner = await hasCompletedBeginner({
        github,
        owner,
        repo,
        username,
    });

    if (!hasBeginner) {
        console.log('[tiers] Exit: missing Beginner completion', {
            username,
        });
        return false;
    }

    console.log('[tiers] Success: user is eligible for Intermediate issues', {
        username,
    });

    return true;
}

module.exports = {
    hasIntermediateEligibility,
};
