/**
 * Determines whether a contributor has completed at least `requiredCount`
 * Beginner issues in the given repository.
 *
 * A Beginner issue is counted when a merged pull request authored by
 * the contributor closes an issue labeled `beginner`.
 *
 * IMPORTANT CONTEXT:
 * - The `beginner` label was introduced on 2026-01-01.
 * - Pull requests merged before that date cannot qualify.
 * - This helper stops scanning once PRs predate the label introduction
 *   to avoid unnecessary API calls.
 *
 * This helper is intentionally generic and parameterized. Policy decisions
 * (for example, whether 1 or more Beginner issues are required) should be
 * expressed at the call site.
 *
 * IMPLEMENTATION NOTES:
 * - Searches merged PRs authored by the contributor (newest → oldest).
 * - Stops scanning once PRs predate the Beginner label introduction date.
 * - Inspects PR timelines to identify issues closed by each PR.
 * - Counts issues labeled `beginner`.
 * - Returns early once the required count is reached.
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github - Authenticated GitHub client
 * @param {string} params.owner - Repository owner
 * @param {string} params.repo - Repository name
 * @param {string} params.username - GitHub username to check
 * @param {number} params.requiredCount - Number of Beginner issues required
 * @returns {Promise<boolean>} Whether the contributor meets the requirement
 */
const BEGINNER_ISSUE_LABEL = 'beginner';

/**
 * Date when the Beginner label began being used in this repository.
 * Used as a hard cutoff to avoid scanning PRs that cannot qualify.
 */
const BEGINNER_LABEL_INTRODUCED_AT = new Date('2026-01-01');

const hasCompletedBeginner = async ({
    github,
    owner,
    repo,
    username,
    requiredCount,
}) => {
    // Log the start of the eligibility check for traceability
    console.log('[has-beginner] Start check:', {
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
    // have completed any Beginner issues.
    if (!prs.length) {
        console.log('[has-beginner] Exit: no merged PRs found');
        return false;
    }

    let completedCount = 0;

    for (const pr of prs) {
        // Prefer `closed_at` when available, as it best represents
        // when the PR was actually merged.
        const mergedAt = new Date(pr.closed_at ?? pr.updated_at);

        // Stop scanning once PRs predate the Beginner label introduction.
        // Older PRs cannot possibly qualify.
        if (mergedAt < BEGINNER_LABEL_INTRODUCED_AT) {
            console.log('[has-beginner] Stop: PR predates Beginner label', {
                prNumber: pr.number,
                mergedAt: mergedAt.toISOString(),
            });
            break;
        }

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

                if (labels.includes(BEGINNER_ISSUE_LABEL)) {
                    completedCount += 1;

                    console.log(
                        '[has-beginner] Found completed Beginner issue',
                        {
                            username,
                            prNumber: pr.number,
                            issueNumber,
                            completedCount,
                        }
                    );

                    // Early exit once the required number of
                    // Beginner issues has been reached.
                    if (completedCount >= requiredCount) {
                        console.log(
                            '[has-beginner] Success: Beginner requirement satisfied',
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
    // Beginner-labeled issues to meet the requirement.
    console.log('[has-beginner] Exit: insufficient completed Beginner issues', {
        username,
        completedCount,
        requiredCount,
    });

    return false;
};

module.exports = {
    BEGINNER_ISSUE_LABEL,
    hasCompletedBeginner,
};
