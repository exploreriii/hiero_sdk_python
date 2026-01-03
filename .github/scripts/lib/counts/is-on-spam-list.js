// Helper to check whether a user is on the repository spam list
//
// The spam list is stored in .github/spam-list.txt
// - One username per line
// - Lines starting with # are treated as comments
//
// This helper is intentionally read-only and cached in-memory
// for the duration of the GitHub Action run.

const SPAM_LIST_PATH = '.github/spam-list.txt';

let cachedSpamSet = null;

async function loadSpamList({ github, owner, repo }) {
    if (cachedSpamSet) {
        return cachedSpamSet;
    }

    try {
        const { data } = await github.rest.repos.getContent({
            owner,
            repo,
            path: SPAM_LIST_PATH,
        });

        const content = Buffer.from(
            data.content,
            data.encoding || 'base64'
        ).toString('utf8');

        const entries = content
            .split('\n')
            .map(line => line.trim())
            .filter(line => line.length > 0)
            .filter(line => !line.startsWith('#'))
            .map(line => line.toLowerCase());

        cachedSpamSet = new Set(entries);

        console.log('[spam-list] Loaded spam list:', {
            count: cachedSpamSet.size,
        });

        return cachedSpamSet;
    } catch (error) {
        if (error?.status === 404) {
            console.log('[spam-list] No spam list found at', SPAM_LIST_PATH);
            cachedSpamSet = new Set();
            return cachedSpamSet;
        }

        console.log('[spam-list] Failed to load spam list:', {
            message: error.message,
        });

        // Fail closed? No.
        // If the spam list cannot be read, do NOT block contributors.
        cachedSpamSet = new Set();
        return cachedSpamSet;
    }
}

async function isOnSpamList({ github, owner, repo, username }) {
    const spamSet = await loadSpamList({ github, owner, repo });

    const isSpam = spamSet.has(username.toLowerCase());

    console.log('[spam-list] Check:', {
        username,
        isSpam,
    });

    return isSpam;
}

module.exports = {
    isOnSpamList,
};
