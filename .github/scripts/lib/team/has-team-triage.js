// Helper to determine whether a user has triage-level or higher permissions
//
// This is useful for:
// - Labeling
// - Moderation
// - Non-privileged workflow actions
//
// NOTE:
// - This does NOT imply exemption from eligibility checks.

const TRIAGE_PERMISSION_LEVELS = ['triage'];

async function isTriager({ github, owner, repo, username }) {
    try {
        const response =
            await github.rest.repos.getCollaboratorPermissionLevel({
                owner,
                repo,
                username,
            });

        const permission =
            response?.data?.permission?.toLowerCase() ?? 'none';

        const isTriager = TRIAGE_PERMISSION_LEVELS.includes(permission);

        console.log('[is-triager] Permission check:', {
            username,
            permission,
            isTriager,
        });

        return isTriager;
    } catch (error) {
        if (error?.status === 404) {
            console.log('[is-triager] User is not a collaborator:', {
                username,
            });
            return false;
        }

        console.log('[is-triager] Permission check failed:', {
            username,
            message: error.message,
        });

        return false;
    }
}

module.exports = {
    isTriager,
};
