// Helper to determine whether a user is a committer-level collaborator
//
// Committers are trusted contributors with code-level access.
// They bypass all eligibility requirements.

const COMMITTER_PERMISSION_LEVELS = ['write', 'maintain', 'admin'];

async function isWriter({ github, owner, repo, username }) {
    try {
        const response =
            await github.rest.repos.getCollaboratorPermissionLevel({
                owner,
                repo,
                username,
            });

        const permission =
            response?.data?.permission?.toLowerCase() ?? 'none';

        const isWriter = COMMITTER_PERMISSION_LEVELS.includes(permission);

        console.log('[is-committer] Permission check:', {
            username,
            permission,
            isWriter,
        });

        return isWriter;
    } catch (error) {
        if (error?.status === 404) {
            console.log('[is-committer] User is not a collaborator:', {
                username,
            });
            return false;
        }

        console.log('[is-committer] Permission check failed:', {
            username,
            message: error.message,
        });

        return false;
    }
}

module.exports = {
    isWriter,
};
