// Helper to determine whether a user is part of the triage, committer, maintainer team.
//
// This is useful for:
// - Labeling
// - Moderation
// - Non-privileged workflow actions
//


const COMMITTER_PERMISSION_LEVELS = ['triage', 'write', 'maintain', 'admin'];

async function isTeam({ github, owner, repo, username }) {
    try {
        const response =
            await github.rest.repos.getCollaboratorPermissionLevel({
                owner,
                repo,
                username,
            });

        const permission =
            response?.data?.permission?.toLowerCase() ?? 'none';

        const isTeamr = TRIAGE_PERMISSION_LEVELS.includes(permission);

        console.log('[is-triager] Permission check:', {
            username,
            permission,
            isTeamr,
        });

        return isTeamr;
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
    isTeamr,
};
