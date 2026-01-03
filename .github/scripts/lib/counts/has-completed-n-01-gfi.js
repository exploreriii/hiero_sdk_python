/**
 * Determines whether a contributor has completed at least `requiredCount`
 * Good First Issues (GFIs) in the given repository.
 *
 * A GFI is counted when a merged pull request authored by the contributor
 * closes an issue labeled `Good First Issue`.
 *
 * IMPORTANT CONTEXT:
 * - The `Good First Issue` label was introduced on 2025-07-14.
 * - Pull requests merged before that date cannot qualify.
 * - This helper stops scanning once PRs predate the label introduction
 *   to avoid unnecessary API calls.
 *
 * This helper is intentionally generic and parameterized. Policy decisions
 * (for example, whether 1 or more GFIs are required) should be expressed
 * at the call site.
 *
 * IMPLEMENTATION NOTES:
 * - Searches merged PRs authored by the contributor (newest → oldest).
 * - Stops scanning once PRs predate the GFI label introduction date.
 * - Inspects PR timelines to identify issues closed by each PR.
 * - Counts issues labeled `Good First Issue`.
 * - Returns early once the required count is reached.
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github - Authenticated GitHub client
 * @param {string} params.owner - Repository owner
 * @param {string} params.repo - Repository name
 * @param {string} params.username - GitHub username to check
 * @param {number} params.requiredCount - Number of Good First Issues required
 * @returns {Promise<boolean>} Whether the contributor meets the requirement
 */
const GOOD_FIRST_ISSUE_LABEL = 'Good First Issue';

/**
 * Date when the Good First Issue label began being used in this repository.
 * Used as a hard cutoff to avoid scanning PRs that cannot qualify.
 */
const GFI_LABEL_INTRODUCED_AT = new Date('2025-07-14');

const hasCompletedGfi = async ({
    github,
    owner,
    repo,
    username,
    requiredCount,
}) => {
    // Log the start of the eligibility check for traceability
    console.log('[has-gfi] Start check:', {
        owner,
        repo,
        username,
        requiredCount,
    });

    // Fetch merged pull requests authored by the contributor.
    // Results are ordered newest → oldest to allow early exits
    // both on success and on label cutoff.
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
    // have completed any Good First Issues.
    if (!prs.length) {
        console.log('[has-gfi] Exit: no merged PRs found');
        return false;
    }

    let completedCount = 0;

    for (const pr of prs) {
        // Prefer `closed_at` when available, as it most accurately
        // represents when the PR was merged.
        const mergedAt = new Date(pr.closed_at ?? pr.updated_at);

        // Stop scanning once PRs predate the GFI label introduction.
        // Older PRs cannot possibly qualify.
        if (mergedAt < GFI_LABEL_INTRODUCED_AT) {
            console.log('[has-gfi] Stop: PR predates GFI label', {
                prNumber: pr.number,
                mergedAt: mergedAt.toISOString(),
            });
            break;
        }

        console.log('[has-gfi] Inspecting PR:', {
            prNumber: pr.number,
            prTitle: pr.title,
        });

        // Inspect the PR timeline to find issues that were closed
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
            // We only care about "closed" events that reference an issue.
            if (
                event.event === 'closed' &&
                event?.source?.issue?.number
            ) {
                const issueNumber = event.source.issue.number;

                // Fetch the linked issue so we can inspect its labels.
                const { data: issue } =
                    await github.rest.issues.get({
                        owner,
                        repo,
                        issue_number: issueNumber,
                    });

                const labels =
                    issue.labels?.map(label => label.name) ?? [];

                if (labels.includes(GOOD_FIRST_ISSUE_LABEL)) {
                    completedCount += 1;

                    console.log(
                        '[has-gfi] Found completed Good First Issue',
                        {
                            username,
                            prNumber: pr.number,
                            issueNumber,
                            completedCount,
                        }
                    );

                    // Early exit once the required number of
                    // Good First Issues has been reached.
                    if (completedCount >= requiredCount) {
                        console.log(
                            '[has-gfi] Success: GFI requirement satisfied',
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
    // Good First Issue–labeled issues to meet the requirement.
    console.log('[has-gfi] Exit: insufficient completed Good First Issues', {
        username,
        completedCount,
        requiredCount,
    });

    return false;
};

module.exports = {
    GOOD_FIRST_ISSUE_LABEL,
    hasCompletedGfi,
};
