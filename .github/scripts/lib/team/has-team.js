/**
 * Determines whether a contributor is part of the repository team
 * with triage-level or higher permissions.
 *
 * This includes users with:
 * - triage
 * - write
 * - maintain
 * - admin
 *
 * This helper is useful for:
 * - Labeling
 * - Moderation
 * - Non-privileged workflow actions
 *
 * IMPORTANT:
 * - This does NOT imply exemption from eligibility or capacity checks.
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
 * @returns {Promise<boolean>} Whether the contributor is a team member
 */
const TEAM_PERMISSION_LEVELS = ['triage', 'write', 'maintain', 'admin'];

const isTeam = async ({
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

        const isTeamMember =
            TEAM_PERMISSION_LEVELS.includes(permission);

        console.log('[is-team] Permission check:', {
            username,
            permission,
            isTeamMember,
        });

        return isTeamMember;
    } catch (error) {
        // 404 indicates the user is not a collaborator on the repo.
        if (error?.status === 404) {
            console.log('[is-team] User is not a collaborator', {
                username,
            });
            return false;
        }

        // Any other error fails closed to avoid granting privileges.
        console.log('[is-team] Permission lookup failed', {
            username,
            message: error.message,
        });

        return false;
    }
};

module.exports = {
    isTeam,
};
