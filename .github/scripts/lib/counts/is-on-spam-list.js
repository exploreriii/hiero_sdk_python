/**
 * Path to the repository-scoped spam list file.
 *
 * The spam list is stored as a plain text file with:
 * - One GitHub username per line
 * - Lines starting with `#` treated as comments
 * - Usernames treated case-insensitively
 */
const SPAM_LIST_PATH = '.github/spam-list.txt';

/**
 * In-memory cache of spam list entries.
 *
 * This cache is intentionally scoped to the lifetime of a single
 * GitHub Action run to avoid repeated API calls and rate limiting.
 *
 * @type {Set<string> | null}
 */
let cachedSpamSet = null;

/**
 * Loads and parses the repository spam list.
 *
 * The spam list is fetched from {@link SPAM_LIST_PATH}, normalized to
 * lowercase, and cached in memory for the duration of the Action run.
 *
 * FAILURE BEHAVIOR:
 * - If the spam list file does not exist, an empty set is returned.
 * - If the spam list cannot be read for any reason, an empty set is
 *   returned (fail open) to avoid blocking contributors.
 *
 * This helper is intentionally read-only and side-effect free
 * aside from populating the in-memory cache.
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github - Authenticated GitHub client
 * @param {string} params.owner - Repository owner
 * @param {string} params.repo - Repository name
 * @returns {Promise<Set<string>>} Set of spam-listed usernames (lowercase)
 */
const loadSpamList = async ({ github, owner, repo }) => {
    // Return the cached spam list if it has already been loaded
    if (cachedSpamSet) {
        return cachedSpamSet;
    }

    try {
        // Fetch the spam list file from the repository
        const { data } = await github.rest.repos.getContent({
            owner,
            repo,
            path: SPAM_LIST_PATH,
        });

        // Decode file contents (GitHub API returns base64 by default)
        const content = Buffer.from(
            data.content,
            data.encoding || 'base64'
        ).toString('utf8');

        // Parse the file into normalized username entries
        const entries = content
            .split('\n')
            .map(line => line.trim())
            // Ignore empty lines
            .filter(line => line.length > 0)
            // Ignore commented lines
            .filter(line => !line.startsWith('#'))
            // Normalize usernames for case-insensitive matching
            .map(line => line.toLowerCase());

        cachedSpamSet = new Set(entries);

        console.log('[spam-list] Loaded spam list', {
            count: cachedSpamSet.size,
        });

        return cachedSpamSet;
    } catch (error) {
        // If the spam list file does not exist, treat it as empty
        if (error?.status === 404) {
            console.log('[spam-list] No spam list found at', SPAM_LIST_PATH);
            cachedSpamSet = new Set();
            return cachedSpamSet;
        }

        // Any other error should fail open to avoid blocking contributors
        console.log('[spam-list] Failed to load spam list', {
            message: error.message,
        });

        cachedSpamSet = new Set();
        return cachedSpamSet;
    }
};

/**
 * Checks whether a contributor is listed in the repository spam list.
 *
 * This helper relies on the cached spam list loaded via {@link loadSpamList}
 * and performs a case-insensitive membership check.
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
    // Ensure the spam list is loaded and cached
    const spamSet = await loadSpamList({ github, owner, repo });

    // Normalize username before lookup
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
