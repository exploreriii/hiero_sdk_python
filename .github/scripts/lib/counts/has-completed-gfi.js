/**
 * Determines whether a contributor has completed a Good First Issue (GFI)
 * in the given repository.
 *
 * A GFI is identified by a merged pull request authored by the contributor
 * that closed an issue labeled `Good First Issue`.
 *
 * IMPORTANT CONTEXT FOR MAINTAINERS:
 * - The `Good First Issue` label was introduced on 2025-07-14.
 * - Pull requests merged before that date cannot qualify.
 * - This helper intentionally stops scanning once PRs predate the label
 *   introduction to avoid unnecessary API calls.
 * - This function mirrors `hasCompletedBeginner` closely to keep onboarding
 *   policy consistent and easy to reason about.
 *
 * IMPLEMENTATION NOTES:
 * - Searches merged PRs authored by the contributor (newest → oldest).
 * - Stops scanning once PRs predate the GFI label introduction date.
 * - Inspects PR timelines to identify issues closed by each PR.
 * - Checks linked issues for the `Good First Issue` label.
 * - Returns early on the first qualifying match.
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github - Authenticated GitHub client
 * @param {string} params.owner - Repository owner
 * @param {string} params.repo - Repository name
 * @param {string} params.username - GitHub username to check
 * @returns {Promise<boolean>} Whether the contributor has completed a GFI
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
}) => {
    console.log('[has-gfi] Start check:', {
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
        console.log('[has-gfi] Exit: no merged PRs found');
        return false;
    }

    for (const pr of prs) {
        // Prefer closed_at when available, as it best represents merge time.
        const mergedAt = new Date(pr.closed_at ?? pr.updated_at);

        // Stop once PRs predate the GFI label introduction.
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

                if (labels.includes(GOOD_FIRST_ISSUE_LABEL)) {
                    console.log('[has-gfi] Success: completed GFI found', {
                        username,
                        prNumber: pr.number,
                        issueNumber,
                    });

                    // Early exit on first qualifying GFI.
                    return true;
                }
            }
        }
    }

    console.log('[has-gfi] Exit: no completed GFI found', {
        username,
    });

    return false;
};

module.exports = {
    GOOD_FIRST_ISSUE_LABEL,
    hasCompletedGfi,
};
