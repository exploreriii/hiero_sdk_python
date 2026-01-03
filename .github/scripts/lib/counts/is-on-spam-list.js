/**
 * Path to the repository-scoped spam list file.
 *
 * The spam list is stored as a plain text file with:
 * - One GitHub username per line
 * - Lines starting with `#` treated as comments
 */
const SPAM_LIST_PATH = '.github/spam-list.txt';

/**
 * In-memory cache of spam list entries.
 *
 * This cache is intentionally scoped to the lifetime of the
 * GitHub Action run to avoid repeated API calls.
 *
 * @type {Set<string> | null}
 */
let cachedSpamSet = null;

/**
 * Loads and parses the repository spam list.
 *
 * The spam list is read from {@link SPAM_LIST_PATH}, normalized to
 * lowercase, and cached in memory for the duration of the Action run.
 *
 * FAILURE BEHAVIOR:
 * - If the spam list file does not exist, an empty set is returned.
 * - If the spam list cannot be read for any reason, an empty set is
 *   returned (fail open) to avoid blocking contributors.
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github - Authenticated GitHub client
 * @param {string} params.owner - Repository owner
 * @param {string} params.repo - Repository name
 * @returns {Promise<Set<string>>} Set of spam-listed usernames (lowercase)
 */
const loadSpamList = async ({ github, owner, repo }) => {
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

        // Fail open: if the spam list cannot be read, do not block contributors.
        cachedSpamSet = new Set();
        return cachedSpamSet;
    }
};

/**
 * Checks whether a contributor is listed in the repository spam list.
 *
 * This helper is read-only and relies on the cached spam list loaded
 * via {@link loadSpamList}.
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github - Authenticated GitHub client
 * @param {string} params.owner - Repository owner
 * @param {string} params.repo - Repository name
 * @param {string} params.username - GitHub username to check
 * @returns {Promise<boolean>} Whether the user is listed as spam
 */
const isOnSpamList = async ({
    github,
    owner,
    repo,
    username,
}) => {
    const spamSet = await loadSpamList({ github, owner, repo });

    const isSpam = spamSet.has(username.toLowerCase());

    console.log('[spam-list] Check:', {
        username,
        isSpam,
    });

    return isSpam;
};

module.exports = {
    isOnSpamList,
};
