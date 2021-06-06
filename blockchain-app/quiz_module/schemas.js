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

module.exports = { CreateQuestionSchema };
