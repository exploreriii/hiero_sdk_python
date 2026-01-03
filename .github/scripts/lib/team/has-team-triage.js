/**
 * Determines whether a contributor has triage-level or higher
 * permissions on the repository.
 *
 * Triage-level contributors can perform moderation actions
 * (labeling, issue management, etc.) but do NOT bypass
 * tier eligibility or capacity checks.
 *
 * FAILURE BEHAVIOR:
 * - If the permission lookup fails for any reason other than
 *   "not a collaborator", this helper fails closed and returns `false`.
 *
 * @param {Object} params
 * @param {import('@actions/github').GitHub} params.github - Authenticated GitHub client
 * @param {string} params.owner - Repository owner
 * @param {string} params.repo - Repository name
 * @param {string} params.username - GitHub username to check
 * @returns {Promise<boolean>} Whether the contributor has triage-level access
 */
const TRIAGE_PERMISSION_LEVELS = ['triage', 'write', 'maintain', 'admin'];

const isTriager = async ({
    github,
    owner,
    repo,
    username,
}) => {
    try {
        // Fetch the collaborator permission level for the user.
        // This endpoint returns the user's highest permission
        // within the repository.
        const { data } =
            await github.rest.repos.getCollaboratorPermissionLevel({
                owner,
                repo,
                username,
            });

        // Normalize permission for safe comparison.
        const permission =
            data?.permission?.toLowerCase() ?? 'none';

        const isTriager =
            TRIAGE_PERMISSION_LEVELS.includes(permission);

        console.log('[is-triager] Permission check:', {
            username,
            permission,
            isTriager,
        });

        return isTriager;
    } catch (error) {
        // 404 indicates the user is not a collaborator on the repo.
        if (error?.status === 404) {
            console.log('[is-triager] User is not a collaborator', {
                username,
            });
            return false;
        }

        // Any other error (API failure, auth issues, etc.)
        // fails closed to avoid granting unintended privileges.
        console.log('[is-triager] Permission lookup failed', {
            username,
            message: error.message,
        });

        return false;
    }
};

module.exports = {
    isTriager,
};
