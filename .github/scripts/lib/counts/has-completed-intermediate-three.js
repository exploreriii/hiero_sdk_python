/**
 * Determines whether a contributor has completed at least `requiredCount`
 * Intermediate issues in the given repository.
 *
 * An Intermediate issue is counted when a merged pull request authored
 * by the contributor closes an issue labeled `intermediate`.
 *
 * This helper is intentionally generic and parameterized. Policy decisions
 * (for example, whether 2 or 3 Intermediate issues are required) should be
 * expressed at the call site, not hard-coded here.
 *
 * IMPLEMENTATION NOTES:
 * - Searches merged PRs authored by the contributor (newest → oldest).
 * - Inspects PR timelines to identify issues closed by each PR.
 * - Counts issues labeled `intermediate`.
 * - Returns early once the required count is reached.
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github - Authenticated GitHub client
 * @param {string} params.owner - Repository owner
 * @param {string} params.repo - Repository name
 * @param {string} params.username - GitHub username to check
 * @param {number} params.requiredCount - Number of Intermediate issues required
 * @returns {Promise<boolean>} Whether the contributor meets the requirement
 */
const INTERMEDIATE_ISSUE_LABEL = 'intermediate';

const hasCompletedIntermediate = async ({
    github,
    owner,
    repo,
    username,
    requiredCount,
}) => {
    // Log the start of the eligibility check for traceability
    console.log('[has-intermediate] Start check:', {
        owner,
        repo,
        username,
        requiredCount,
    });

    // Fetch merged pull requests authored by the contributor.
    // Results are ordered newest → oldest to allow early exits
    // once the required number of Intermediate issues is found.
    const prs = await github.paginate(
        github.rest.search.issuesAndPullRequests,
        {
            q: `is:pr is:merged author:${username} repo:${owner}/${repo}`,
            sort: 'updated',
            order: 'desc',
            per_page: 50,
        }
    );

    // If the contributor has never merged a PR, they cannot
    // have completed any Intermediate issues.
    if (!prs.length) {
        console.log('[has-intermediate] Exit: no merged PRs found');
        return false;
    }

    let completedCount = 0;

    // Inspect each merged PR to determine whether it closed
    // one or more Intermediate-labeled issues.
    for (const pr of prs) {
        // Fetch the PR timeline to identify issues that were closed
        // as a result of this PR being merged.
        const timeline = await github.paginate(
            github.rest.issues.listEventsForTimeline,
            {
                owner,
                repo,
                issue_number: pr.number,
                per_page: 100,
            }
        );

        for (const event of timeline) {
            // We only care about "closed" events that reference an issue
            if (
                event.event === 'closed' &&
                event?.source?.issue?.number
            ) {
                const issueNumber = event.source.issue.number;

                // Fetch the linked issue so we can inspect its labels.
                // If the issue is labeled `intermediate`, it counts
                // toward the contributor's Intermediate requirement.
                const { data: issue } =
                    await github.rest.issues.get({
                        owner,
                        repo,
                        issue_number: issueNumber,
                    });

                const labels =
                    issue.labels?.map(label => label.name) ?? [];

                if (labels.includes(INTERMEDIATE_ISSUE_LABEL)) {
                    completedCount += 1;

                    console.log(
                        '[has-intermediate] Found completed Intermediate issue',
                        {
                            username,
                            prNumber: pr.number,
                            issueNumber,
                            completedCount,
                        }
                    );

                    // Early exit once the required number of
                    // Intermediate issues has been reached.
                    if (completedCount >= requiredCount) {
                        console.log(
                            '[has-intermediate] Success: Intermediate requirement satisfied',
                            {
                                username,
                                completedCount,
                                requiredCount,
                            }
                        );

                        return true;
                    }
                }
            }
        }
    }

    // Contributor has merged PRs, but not enough that close
    // Intermediate-labeled issues to meet the requirement.
    console.log('[has-intermediate] Exit: insufficient completed Intermediate issues', {
        username,
        completedCount,
        requiredCount,
    });

    return false;
};

module.exports = {
    INTERMEDIATE_ISSUE_LABEL,
    hasCompletedIntermediate,
};
