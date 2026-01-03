/**
 * Determines whether a contributor has completed at least `requiredCount`
 * Advanced issues in the given repository.
 *
 * An Advanced issue is counted when a merged pull request authored by
 * the contributor closes an issue labeled `advanced`.
 *
 * This helper is intentionally generic and parameterized. Policy decisions
 * (for example, whether 1 or more Advanced issues are required) should be
 * expressed at the call site.
 *
 * IMPLEMENTATION NOTES:
 * - Searches merged PRs authored by the contributor (newest → oldest).
 * - Inspects PR timelines to identify issues closed by each PR.
 * - Counts issues labeled `advanced`.
 * - Returns early once the required count is reached.
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github - Authenticated GitHub client
 * @param {string} params.owner - Repository owner
 * @param {string} params.repo - Repository name
 * @param {string} params.username - GitHub username to check
 * @param {number} params.requiredCount - Number of Advanced issues required
 * @returns {Promise<boolean>} Whether the contributor meets the requirement
 */
const ADVANCED_ISSUE_LABEL = 'advanced';

const hasCompletedAdvanced = async ({
    github,
    owner,
    repo,
    username,
    requiredCount,
}) => {
    // Log the start of the eligibility check for traceability
    console.log('[has-advanced] Start check:', {
        owner,
        repo,
        username,
        requiredCount,
    });

    // Fetch merged pull requests authored by the contributor.
    // Results are ordered newest → oldest to allow early exits
    // once the required number of Advanced issues is found.
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
    // have completed any Advanced issues.
    if (!prs.length) {
        console.log('[has-advanced] Exit: no merged PRs found');
        return false;
    }

    let completedCount = 0;

    // Inspect each merged PR to determine whether it closed
    // one or more Advanced-labeled issues.
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
                // If the issue is labeled `advanced`, it counts toward
                // the contributor's Advanced requirement.
                const { data: issue } =
                    await github.rest.issues.get({
                        owner,
                        repo,
                        issue_number: issueNumber,
                    });

                const labels =
                    issue.labels?.map(label => label.name) ?? [];

                if (labels.includes(ADVANCED_ISSUE_LABEL)) {
                    completedCount += 1;

                    console.log(
                        '[has-advanced] Found completed Advanced issue',
                        {
                            username,
                            prNumber: pr.number,
                            issueNumber,
                            completedCount,
                        }
                    );

                    // Early exit once the required number of
                    // Advanced issues has been reached.
                    if (completedCount >= requiredCount) {
                        console.log(
                            '[has-advanced] Success: Advanced requirement satisfied',
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
    // Advanced-labeled issues to meet the requirement.
    console.log('[has-advanced] Exit: insufficient completed Advanced issues', {
        username,
        completedCount,
        requiredCount,
    });

    return false;
};

module.exports = {
    ADVANCED_ISSUE_LABEL,
    hasCompletedAdvanced,
};
