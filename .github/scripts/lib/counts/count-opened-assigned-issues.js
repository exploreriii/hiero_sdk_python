/**
 * Counts the number of open GitHub issues currently assigned to a user
 * within a specific repository.
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
const countOpenAssignedIssues = async ({
    github,
    owner,
    repo,
    username,
}) => {
    // Log the start of the check for traceability in Action logs
    console.log('[count-open-assigned-issues] Start check:', {
        owner,
        repo,
        username,
    });

    try {
        // Use GitHub's search API to count open issues (not PRs)
        // assigned to the given user within this repository.
        //
        // NOTE:
        // - `is:issue` excludes pull requests
        // - `is:open` ensures only active issues are counted
        // - The search API returns a `total_count`, which avoids
        //   fetching and paginating individual issues.
        const { data } = await github.rest.search.issuesAndPullRequests({
            q: [
                `repo:${owner}/${repo}`,
                'is:issue',
                'is:open',
                `assignee:${username}`,
            ].join(' '),
        });

        // Safely extract the count, defaulting to 0 if missing
        const count = data?.total_count ?? 0;

        // Log the computed result for debugging and audits
        console.log('[count-open-assigned-issues] Result:', {
            username,
            count,
        });

        return count;
    } catch (error) {
        // Log the error but do not throw
        console.log('[count-open-assigned-issues] Error:', {
            username,
            message: error.message,
        });

        // Fail open by returning a very large number so callers
        // treat this as "over the limit" and block new assignments.
        return Number.MAX_SAFE_INTEGER;
    }
};

module.exports = {
    countOpenAssignedIssues,
};
