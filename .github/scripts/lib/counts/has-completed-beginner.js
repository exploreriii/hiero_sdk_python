/**
 * Determines whether a contributor has completed a Beginner issue
 * in the given repository.
 *
 * A Beginner issue represents the second onboarding step after
 * Good First Issues. This helper checks for merged pull requests
 * authored by the contributor that closed an issue labeled
 * `beginner`.
 *
 * IMPORTANT CONTEXT FOR MAINTAINERS:
 * - The `beginner` label predates Intermediate issues.
 * - Older Beginner issue completions are intentionally counted.
 * - This helper intentionally mirrors `has-gfi.js` to keep onboarding
 *   policy consistent and easy to reason about.
 * - If logic here changes, `has-gfi.js` should likely be reviewed.
 *
 * IMPLEMENTATION NOTES:
 * - Searches merged PRs authored by the contributor.
 * - Inspects PR timelines to find linked closed issues.
 * - Checks linked issues for the `beginner` label.
 * - Returns early on the first qualifying match.
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github - Authenticated GitHub client
 * @param {string} params.owner - Repository owner
 * @param {string} params.repo - Repository name
 * @param {string} params.username - GitHub username to check
 * @returns {Promise<boolean>} Whether the contributor has completed a Beginner issue
 */
const BEGINNER_ISSUE_LABEL = 'beginner';

/**
 * Checks whether a contributor has completed at least one Beginner issue.
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github
 * @param {string} params.owner
 * @param {string} params.repo
 * @param {string} params.username
 * @returns {Promise<boolean>}
 */
const hasCompletedBeginner = async ({
    github,
    owner,
    repo,
    username,
}) => {
    console.log('[has-beginner] Start check:', {
        owner,
        repo,
        username,
    });

    // Fetch merged PRs authored by the contributor, newest first.
    const prs = await github.paginate(
        github.rest.search.issuesAndPullRequests,
        {
            q: `is:pr is:merged author:${username} repo:${owner}/${repo}`,
            sort: 'updated',
            order: 'desc',
            per_page: 50,
        }
    );

    if (!prs.length) {
        console.log('[has-beginner] Exit: no merged PRs found');
        return false;
    }

    for (const pr of prs) {
        console.log('[has-beginner] Inspecting PR:', {
            prNumber: pr.number,
            prTitle: pr.title,
        });

        // Inspect PR timeline events to find issues closed by this PR.
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
            if (
                event.event === 'closed' &&
                event?.source?.issue?.number
            ) {
                const issueNumber = event.source.issue.number;

                // Fetch the linked issue to inspect its labels.
                const { data: issue } =
                    await github.rest.issues.get({
                        owner,
                        repo,
                        issue_number: issueNumber,
                    });

                const labels =
                    issue.labels?.map(label => label.name) ?? [];

                if (labels.includes(BEGINNER_ISSUE_LABEL)) {
                    console.log(
                        '[has-beginner] Success: completed Beginner issue found',
                        {
                            username,
                            prNumber: pr.number,
                            issueNumber,
                        }
                    );

                    // Early exit on first qualifying Beginner issue.
                    return true;
                }
            }
        }
    }

    console.log(
        '[has-beginner] Exit: no completed Beginner issue found',
        { username }
    );

    return false;
};

module.exports = {
    BEGINNER_ISSUE_LABEL,
    hasCompletedBeginner,
};
