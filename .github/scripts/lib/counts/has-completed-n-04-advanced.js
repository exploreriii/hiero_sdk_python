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
 * IMPORTANT CONTEXT:
 * - The `advanced` label was introduced at a known point in time.
 * - Pull requests merged before the label introduction date cannot qualify.
 * - This helper stops scanning once PRs predate the label introduction
 *   to avoid unnecessary API calls.
 *
 * IMPLEMENTATION NOTES:
 * - Searches merged PRs authored by the contributor (newest → oldest).
 * - Stops scanning once PRs predate the Advanced label introduction date.
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

/**
 * Date when the Advanced label began being used in this repository.
 * Used as a hard cutoff to avoid scanning PRs that cannot qualify.
 *
 * NOTE:
 * If this date changes, update it alongside any documentation
 * describing Advanced issue eligibility.
 */
const ADVANCED_LABEL_INTRODUCED_AT = new Date('2025-12-05');

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
    // have completed any Advanced issues.
    if (!prs.length) {
        console.log('[has-advanced] Exit: no merged PRs found');
        return false;
    }

    let completedCount = 0;

    for (const pr of prs) {
        // Prefer `closed_at` when available, as it best represents
        // when the PR was actually merged.
        const mergedAt = new Date(pr.closed_at ?? pr.updated_at);

        // Stop scanning once PRs predate the Advanced label introduction.
        if (mergedAt < ADVANCED_LABEL_INTRODUCED_AT) {
            console.log('[has-advanced] Stop: PR predates Advanced label', {
                prNumber: pr.number,
                mergedAt: mergedAt.toISOString(),
            });
            break;
        }

        // Inspect the PR timeline to identify issues closed by this PR
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

                // Fetch the linked issue so we can inspect its labels
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
