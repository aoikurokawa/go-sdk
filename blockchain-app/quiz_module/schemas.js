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
    }
}

module.exports = { CreateQuestionSchema, AnswerQuestionSchema };
