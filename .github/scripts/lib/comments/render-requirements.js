// comments/renderRequirements.js
const { ELIGIBILITY_REQUIREMENTS } =
    require('../eligibility/requirements');

const renderRequirements = ({
    issueType,
    stats, // counts collected by caller
}) => {
    const req = ELIGIBILITY_REQUIREMENTS[issueType];
    const lines = [];

    if (req.capacity) {
        const max =
            typeof req.capacity === 'object'
                ? req.capacity.maxOpenIssues
                : stats.maxAllowed;

        lines.push(
            `- Open assignments: **${stats.openAssignedCount} / ${max}**`
        );
    }

    for (const prereq of req.prerequisites || []) {
        const actual = stats[`${prereq.type}Completed`] ?? 0;
        const met = actual >= prereq.requiredCount;

        lines.push(
            `- ${prereq.type} issues completed: **${actual} / ${prereq.requiredCount}** ${met ? '✅' : '❌'}`
        );
    }

    return lines.join('\n');
};

module.exports = { renderRequirements };
