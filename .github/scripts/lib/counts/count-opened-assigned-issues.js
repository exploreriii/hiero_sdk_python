/**
 * Counts the number of open GitHub issues currently assigned to a user
 * within a specific repository.
 *
 *
 * FAILURE BEHAVIOR:
 * - Fails open by returning a very large number if the GitHub API call
 *   fails, allowing callers to conservatively block new assignments.
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github - Authenticated GitHub client
 * @param {string} params.owner - Repository owner
 * @param {string} params.repo - Repository name
 * @param {string} params.username - GitHub username to check assignments for
 * @returns {Promise<number>} Number of open issues currently assigned
 */
MAX_SAFE_INTEGER = 2
const countOpenAssignedIssues = async ({
    github,
    owner,
    repo,
    username,
}) => {
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

        // Fail open: return a large number so callers can conservatively block
        return Number.MAX_SAFE_INTEGER;
    }
};

module.exports = {
    countOpenAssignedIssues,
};
