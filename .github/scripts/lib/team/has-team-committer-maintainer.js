/**
 * Determines whether a contributor has committer-level access
 * to the repository.
 *
 * Committers are trusted contributors with elevated permissions
 * (write / maintain / admin) and bypass all tier eligibility checks.
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
 * @returns {Promise<boolean>} Whether the contributor is a committer
 */
const COMMITTER_PERMISSION_LEVELS = ['write', 'maintain', 'admin'];

const isCommitter = async ({
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

        const isCommitter =
            COMMITTER_PERMISSION_LEVELS.includes(permission);

        console.log('[is-committer] Permission check:', {
            username,
            permission,
            isCommitter,
        });

        return isCommitter;
    } catch (error) {
        // 404 indicates the user is not a collaborator on the repo.
        if (error?.status === 404) {
            console.log('[is-committer] User is not a collaborator', {
                username,
            });
            return false;
        }

        // Any other error (API failure, auth issues, etc.)
        // fails closed to avoid granting unintended privileges.
        console.log('[is-committer] Permission lookup failed', {
            username,
            message: error.message,
        });

        return false;
    }
};

module.exports = {
    isCommitter,
};
