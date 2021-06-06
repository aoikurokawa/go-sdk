const CreateQuestionSchema = {
    $id: 'lisk/question/create',
    type: 'object',
    required: ["question", "answer", "reward"],
    properties: {
        question: {
            datatType: "string",
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

const AnswerQuestionSchema = {
    $id: 'lisk/question/answer',
    type: 'object',
    required: ['questionId', 'answer'],
    properties: {
        questionId: {
            datatType: 'bytes',
            fieldNumber: 1,
        },
        answer: {
            dataType: 'string',
            fieldNumber: 2,
        },
    },
};

const QuestionAccountSchema = {
    type: 'object', 
    required: ['ownQuestions'],
    properties: {
        ownQuestions: {
            type: 'array', 
            fieldNumber: 1,
            items: {
                datatType: "bytes",
            },
        },
    },
    default: {
        ownQuestions: [],
    },
};

module.exports = { CreateQuestionSchema, AnswerQuestionSchema, QuestionAccountSchema };
