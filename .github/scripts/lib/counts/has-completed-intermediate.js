// Reusable function to check if a user has completed an Intermediate issue

const INTERMEDIATE_ISSUE_LABEL = 'intermediate';

async function hasCompletedIntermediate({ github, owner, repo, username }) {
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
                    issue.labels?.map(l => l.name) ?? [];

                if (labels.includes(INTERMEDIATE_ISSUE_LABEL)) {
                    console.log('[has-intermediate] Success: completed Intermediate issue found', {
                        username,
                        prNumber: pr.number,
                        issueNumber,
                    });

                    return true;
                }
            }
        }
    }

    console.log('[has-intermediate] Exit: no completed Intermediate issue found', {
        username,
    });

    return false;
}

module.exports = {
    INTERMEDIATE_ISSUE_LABEL,
    hasCompletedIntermediate,
};
