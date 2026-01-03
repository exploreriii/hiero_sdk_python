/**
 * Determines whether a contributor has completed at least one
 * Intermediate issue in the given repository.
 *
 * An Intermediate issue is counted when a merged pull request authored
 * by the contributor closes an issue labeled `intermediate`.
 *
 * This helper is used for eligibility checks that require prior
 * Intermediate-level experience.
 *
 * IMPLEMENTATION NOTES:
 * - Searches merged PRs authored by the contributor (newest → oldest).
 * - Inspects PR timelines to identify issues closed by each PR.
 * - Checks linked issues for the `intermediate` label.
 * - Returns early on the first qualifying match.
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github - Authenticated GitHub client
 * @param {string} params.owner - Repository owner
 * @param {string} params.repo - Repository name
 * @param {string} params.username - GitHub username to check
 * @returns {Promise<boolean>} Whether the contributor has completed an Intermediate issue
 */
const INTERMEDIATE_ISSUE_LABEL = 'intermediate';

const hasCompletedIntermediate = async ({
    github,
    owner,
    repo,
    username,
}) => {
    console.log('[has-intermediate] Start check:', {
        owner,
        repo,
        username,
    });

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
        console.log('[has-intermediate] Exit: no merged PRs found');
        return false;
    }

    for (const pr of prs) {
        console.log('[has-intermediate] Inspecting PR:', {
            prNumber: pr.number,
            prTitle: pr.title,
        });

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

                const { data: issue } =
                    await github.rest.issues.get({
                        owner,
                        repo,
                        issue_number: issueNumber,
                    });

                const labels =
                    issue.labels?.map(label => label.name) ?? [];

                if (labels.includes(INTERMEDIATE_ISSUE_LABEL)) {
                    console.log(
                        '[has-intermediate] Success: completed Intermediate issue found',
                        {
                            username,
                            prNumber: pr.number,
                            issueNumber,
                        }
                    );

                    return true;
                }
            }
        }
    }

    console.log(
        '[has-intermediate] Exit: no completed Intermediate issue found',
        { username }
    );

    return false;
};

module.exports = {
    INTERMEDIATE_ISSUE_LABEL,
    hasCompletedIntermediate,
};
