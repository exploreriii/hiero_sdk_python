/**
 * Determines whether a contributor is a member of the repository’s
 * triage team **only**.
 *
 * This helper returns true **only if** the contributor’s highest
 * permission level is exactly `triage`.
 *
 * IMPORTANT:
 * - Committers (write / maintain / admin) are intentionally excluded.
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
 * @returns {Promise<boolean>} Whether the contributor is a triage-only member
 */
const TRIAGE_PERMISSION_LEVEL = 'triage';

const isTriager = async ({
    github,
    owner,
    repo,
    username,
}) => {
    try {
        // Fetch the collaborator permission level for the user, expect some to have triage.
        // This returns the user's highest effective permission.
        const { data } =
            await github.rest.repos.getCollaboratorPermissionLevel({
                owner,
                repo,
                username,
            });

        const permission =
            data?.permission?.toLowerCase() ?? 'none';

        const isTriager = permission === TRIAGE_PERMISSION_LEVEL;

        console.log('[is-triager] Permission check:', {
            username,
            permission,
            isTriager,
        });

        return isTriager;
    } catch (error) {
        // 404 indicates the user is not a collaborator.
        if (error?.status === 404) {
            console.log('[is-triager] User is not a collaborator', {
                username,
            });
            return false;
        }

        // Fail closed to avoid granting unintended privileges.
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
