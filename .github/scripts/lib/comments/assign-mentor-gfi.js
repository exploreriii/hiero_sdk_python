const COMMENT_MARKER =
    process.env.COMMENT_MARKER || '<!-- Mentor Assignment Bot -->';

const MENTOR_TEAM =
    process.env.MENTOR_TEAM_ALIAS || '@hiero-ledger/hiero-sdk-python-triage';

const SUPPORT_TEAM =
    process.env.SUPPORT_TEAM_ALIAS ||
    '@hiero-ledger/hiero-sdk-good-first-issue-support';

const buildMentorComment = ({ mentee, mentor, owner, repo }) => `
${COMMENT_MARKER}
👋 Hi @${mentee}, welcome!

Your on-call mentor today is @${mentor} from ${MENTOR_TEAM}.

**How to proceed**
- Review the issue carefully
- Ask questions early
- Share progress often

Need backup? ${SUPPORT_TEAM} is here too.

**Mentor:** @${mentor}
**Mentee:** @${mentee}

⭐ If you enjoy this repo, consider starring it:
https://github.com/${owner}/${repo}
`;

module.exports = { buildMentorComment, COMMENT_MARKER };
