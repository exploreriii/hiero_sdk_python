// Reusable function to check if a user has completed at least
// TWO Intermediate issues

const INTERMEDIATE_ISSUE_LABEL = 'intermediate';
const REQUIRED_INTERMEDIATE_COUNT = 3;

async function hasCompletedIntermediate({ github, owner, repo, username }) {
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
                    issue.labels?.map(l => l.name) ?? [];

                if (labels.includes(INTERMEDIATE_ISSUE_LABEL)) {
                    completedCount += 1;

                    console.log('[has-intermediate] Found completed Intermediate issue', {
                        username,
                        prNumber: pr.number,
                        issueNumber,
                        completedCount,
                    });

                    // Early exit once requirement is met
                    if (completedCount >= REQUIRED_INTERMEDIATE_COUNT) {
                        console.log('[has-intermediate] Success: Intermediate requirement satisfied', {
                            username,
                            completedCount,
                        });

                        return true;
                    }

                    // Important: continue scanning in case the user has
                    // completed another Intermediate issue in a different PR
                }
            }
        }
    }

    console.log('[has-intermediate] Exit: insufficient completed Intermediate issues', {
        username,
        completedCount,
        required: REQUIRED_INTERMEDIATE_COUNT,
    });

    return false;
}

module.exports = {
    INTERMEDIATE_ISSUE_LABEL,
    hasCompletedIntermediate,
};
