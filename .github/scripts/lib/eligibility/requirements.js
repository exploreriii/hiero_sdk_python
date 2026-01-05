const ISSUE_TYPES = {
    GFI: 'gfi',
    BEGINNER: 'beginner',
    INTERMEDIATE: 'intermediate',
    ADVANCED: 'advanced',
};

const ELIGIBILITY_REQUIREMENTS = {
    [ISSUE_TYPES.GFI]: {
        bypass: {
            team: true,
        },
        spamPolicy: {
            allowed: true,
            maxOpenIssues: {
                spamListed: 1,
                normal: 2,
            },
        },
        capacity: true,
        prerequisites: [],
    },

    [ISSUE_TYPES.BEGINNER]: {
        bypass: {
            team: true,
        },
        spamPolicy: {
            allowed: false,
        },
        capacity: {
            maxOpenIssues: 2,
        },
        prerequisites: [
            {
                type: 'gfi',
                requiredCount: 1,
            },
        ],
    },

    [ISSUE_TYPES.INTERMEDIATE]: {
        bypass: {
            team: true,
        },
        spamPolicy: {
            allowed: false,
        },
        capacity: {
            maxOpenIssues: 2,
        },
        prerequisites: [
            {
                type: 'beginner',
                requiredCount: 1,
            },
        ],
    },

    [ISSUE_TYPES.ADVANCED]: {
        bypass: {
            committer: true,
        },
        spamPolicy: {
            allowed: false,
        },
        capacity: {
            maxOpenIssues: 2,
        },
        prerequisites: [
            {
                type: 'intermediate',
                requiredCount: 1,
            },
        ],
    },
};

module.exports = {
    ISSUE_TYPES,
    ELIGIBILITY_REQUIREMENTS,
};
