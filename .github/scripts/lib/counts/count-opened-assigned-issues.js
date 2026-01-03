// Helper to count how many open issues a user is currently assigned to
// in this repository.
//
// Notes:
// - Counts ISSUES only (not PRs)
// - Counts OPEN issues only
// - Repo-scoped by design
// - Intended for policy enforcement (e.g. max concurrent issues)

async function countOpenAssignedIssues({ github, owner, repo, username }) {
    console.log('[count-open-assigned-issues] Start check:', {
        owner,
        repo,
        username,
    });

    try {
        const { data } = await github.rest.search.issuesAndPullRequests({
            q: [
                `repo:${owner}/${repo}`,
                'is:issue',
                'is:open',
                `assignee:${username}`,
            ].join(' '),
        });

        const count = data?.total_count ?? 0;

        console.log('[count-open-assigned-issues] Result:', {
            username,
            count,
        });

        return count;
    } catch (error) {
        console.log('[count-open-assigned-issues] Error:', {
            username,
            message: error.message,
        });

        // Fail closed or open?
        // We FAIL OPEN here: return a high number so bots can conservatively block.
        return Number.MAX_SAFE_INTEGER;
    }
}

module.exports = {
    countOpenAssignedIssues,
};
