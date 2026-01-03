/**
 * Determines whether a contributor has completed the required number
 * of Intermediate issues in the given repository.
 *
 * An Intermediate issue is counted when a merged pull request authored
 * by the contributor closes an issue labeled `intermediate`.
 *
 * This helper is used for eligibility checks (for example, gating
 * access to advanced issues).
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
 * @returns {Promise<boolean>} Whether the contributor meets the Intermediate requirement
 */
const INTERMEDIATE_ISSUE_LABEL = 'intermediate';

/**
 * Number of completed Intermediate issues required to qualify.
 */
const REQUIRED_INTERMEDIATE_COUNT = 3;

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
        required: REQUIRED_INTERMEDIATE_COUNT,
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

    let completedCount = 0;

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

                    // Early exit once the requirement is met.
                    if (completedCount >= REQUIRED_INTERMEDIATE_COUNT) {
                        console.log(
                            '[has-intermediate] Success: Intermediate requirement satisfied',
                            {
                                username,
                                completedCount,
                            }
                        );

                        return true;
                    }
                }
            }
        }
    }

    console.log(
        '[has-intermediate] Exit: insufficient completed Intermediate issues',
        {
            username,
            completedCount,
            required: REQUIRED_INTERMEDIATE_COUNT,
        }
    );

    return false;
};

module.exports = {
    INTERMEDIATE_ISSUE_LABEL,
    hasCompletedIntermediate,
};
