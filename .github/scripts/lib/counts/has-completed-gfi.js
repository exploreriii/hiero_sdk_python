// Reusable function to check if a user has completed a Good First Issue (GFI)
//
// IMPORTANT CONTEXT FOR MAINTAINERS:
// - The "Good First Issue" label was introduced in October 2025.
// - Any PR merged before that date cannot possibly close a GFI.
// - This function is intentionally optimized to stop scanning once PRs
//   predate the label introduction to avoid unnecessary API calls.
//

const GOOD_FIRST_ISSUE_LABEL = 'Good First Issue';

// Date when the GFI label started being used in this repository.
// Used as a hard cutoff to avoid scanning older PRs that cannot qualify.
const GFI_LABEL_INTRODUCED_AT = new Date('2025-07-14');

async function hasCompletedGfi({ github, owner, repo, username }) {
    console.log('[has-gfi] Start check:', {
        owner,
        repo,
        username,
    });

    // Fetch merged PRs authored by the user, sorted newest → oldest.
    // Stop as soon as we reach PRs older than the GFI label.
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
        // Prefer closed_at when available, as it better represents
        // when the PR was actually merged.
        const mergedAt = new Date(pr.closed_at ?? pr.updated_at);

        // Once we reach PRs older than the GFI label introduction,
        // we can safely stop. 
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

        // Inspect the PR timeline to find issues closed by this PR.
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
                // If the issue has the GFI label, the user qualifies
                // and we can immediately return true.
                const { data: issue } =
                    await github.rest.issues.get({
                        owner,
                        repo,
                        issue_number: issueNumber,
                    });

                const labels =
                    issue.labels?.map(l => l.name) ?? [];

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
}

module.exports = {
    GOOD_FIRST_ISSUE_LABEL,
    hasCompletedGfi,
};
