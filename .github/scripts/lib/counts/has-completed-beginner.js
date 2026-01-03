// Reusable function to check if a user has completed a Beginner Issue
//
// IMPORTANT CONTEXT FOR MAINTAINERS:
// - The "beginner" label predates Intermediate issues and represents
//   a contributor’s second onboarding step after Good First Issues.
// - This function mirrors has-gfi.js closely on purpose so that
//   onboarding policy remains consistent and easy to reason about.
// - If you change logic here, you should very likely review has-gfi.js too.
//

const BEGINNER_ISSUE_LABEL = 'beginner';

// NOTE:
// We intentionally do NOT apply a hard cutoff date here.
// Beginner issues existed before Intermediate issues were introduced,
// and older Beginner completions should still count.
async function hasCompletedBeginner({ github, owner, repo, username }) {
    console.log('[has-beginner] Start check:', {
        owner,
        repo,
        username,
    });

    // Fetch merged PRs authored by the user, sorted newest → oldest.
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
                // If the issue has the Beginner label, the user qualifies
                // and we can immediately return true.
                const { data: issue } =
                    await github.rest.issues.get({
                        owner,
                        repo,
                        issue_number: issueNumber,
                    });

                const labels =
                    issue.labels?.map(l => l.name) ?? [];

                if (labels.includes(BEGINNER_ISSUE_LABEL)) {
                    console.log('[has-beginner] Success: completed Beginner issue found', {
                        username,
                        prNumber: pr.number,
                        issueNumber,
                    });

                    // Early exit on first qualifying Beginner issue.
                    return true;
                }
            }
        }
    }

    console.log('[has-beginner] Exit: no completed Beginner issue found', {
        username,
    });

    return false;
}

module.exports = {
    BEGINNER_ISSUE_LABEL,
    hasCompletedBeginner,
};
