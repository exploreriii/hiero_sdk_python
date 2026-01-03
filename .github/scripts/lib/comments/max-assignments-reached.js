// Capacity-related bot messages
//
// Used when a user exceeds the maximum number of open
// issue assignments allowed across the repository.

function capacityLimitReached({ username, openAssignedCount, maxAllowed }) {
    return `Hi @${username}! 👋

You currently have **${openAssignedCount} open issues** assigned.

To keep things manageable for everyone, contributors can have **at most ${maxAllowed} open issues** assigned at a time.

Once you complete or unassign one of your current issues, feel free to come back and request another 👍`;
}

module.exports = {
    capacityLimitReached,
};
