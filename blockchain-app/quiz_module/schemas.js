const createQuizSchema = {
    $id: 'lisk/quiz/create',
    type: 'object',
    required: ["question", "answer", "reward"],
    properties: {
        question: {
            dataType: "string",
            fieldNumber: 1,
        },
        answer: {
            dataType: "string",
            fieldNumber: 2,
        },
        reward: {
            dataType: "uint64",
            fieldNumber: 3,
        },
    },
};

const answerQuizSchema = {
    $id: 'lisk/quiz/answer',
    type: "object",
    required: ['questionId', 'answer'],
    properties: {
        questionId: {
            dataType: 'bytes',
            fieldNumber: 1,
        },
        answer: {
            dataType: 'string',
            fieldNumber: 2,
        },
    },
};

const quizAccountSchema = {
    type: "object", 
    required: ["ownQuizzes"],
    properties: {
        ownQuizzes: {
            type: "array", 
            fieldNumber: 1,
            items: {
                dataType: "bytes",
            },
        },
    },
    default: {
        ownQuizzes: [],
    },
};

const registeredQuizSchema = {
    $id: 'lisk/quiz/registeredQuestions',
    type: 'object',
    required: ['registeredQuestions'],
    properties: {
        registeredQuestions: {
            type: "array",
            fieldNumber: 1,
            items: {
                type: "object",
                required: ["id", "question", "answer", "reward"],
                properties: {
                    id: {
                        dataType: 'bytes',
                        fieldNumber: 1,
                    },
                    question: {
                        dataType: 'string',
                        fieldNumber: 2,
                    },
                    answer: {
                        dataType: 'string',
                        fieldNumber: 3,
                    },
                    reward: {
                        dataType: 'uint64',
                        fieldNumber: 4,
                    },
                    ownerAddress: {
                        dataType: 'bytes',
                        fieldNumber: 5,
                    },
                },
            },
        },
    },
};

module.exports = { createQuizSchema, answerQuizSchema, quizAccountSchema, registeredQuizSchema };
