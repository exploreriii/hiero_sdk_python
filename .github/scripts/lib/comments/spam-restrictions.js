// Spam-related bot messages
//
// These messages are used when a user is on the repository spam list.
// They are intentionally strict and mirror the legacy bash-based
// Assignment Bot wording exactly.

function spamNonGfiAssignment(username) {
    return `Hi @${username}, this is the Assignment Bot. 

:warning: **Assignment Restricted**

Your account currently has limited assignment privileges. You may only be assigned to issues labeled **Good First Issue**. 

**Current Restrictions:**
- :white_check_mark: Can be assigned to 'Good First Issue' labeled issues (maximum 1 at a time)
- :x: Cannot be assigned to other issues

**How to have restrictions lifted:**
1. Successfully complete and merge your assigned Good First Issue
2. Demonstrate consistent, quality contributions
3. Contact a maintainer to review your restriction status

Thank you for your understanding!`;
}

function spamAssignmentLimitExceeded(username, openCount) {
    return `Hi @${username}, this is the Assignment Bot.

:warning: **Assignment Limit Exceeded**

Your account currently has limited assignment privileges with a maximum of **1 open assignment** at a time.

You currently have ${openCount} open issue(s) assigned.  Please complete and merge your existing assignment before requesting a new one.

**Current Restrictions:**
- Maximum 1 open assignment at a time
- Can only be assigned to 'Good First Issue' labeled issues

**How to have restrictions lifted:**
1. Successfully complete and merge your current assigned issue
2. Demonstrate consistent, quality contributions
3. Contact a maintainer to review your restriction status

Thank you for your cooperation!`;
}

module.exports = {
    spamNonGfiAssignment,
    spamAssignmentLimitExceeded,
};
