const { codec, cryptography } = require("lisk-sdk");

const registeredQuestionSchema = {
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

const CHAIN_STATE_QUESTION = "quiz:registeredQuestions";

const createQuestion = ({ question, answer, reward, ownerAddress, nonce }) => {
    const nonceBuffer = Buffer.alloc(8);
    nonceBuffer.writeBigInt64LE(nonce);

    const seed = Buffer.concat([ownerAddress, nonceBuffer]);
    const id = cryptography.hash(seed);

    return {
        id,
        question,
        answer,
        reward,
        ownerAddress,
    };
};

const getAllQuestions = async (stateStore) => {
    const registeredQuestionsBuffer = await stateStore.chain.get(CHAIN_STATE_QUESTION);
    if (!registeredQuestionsBuffer) {
        return [];
    }   
    const registeredQuestions = codec.decode(registeredQuestionSchema, registeredQuestionsBuffer);

    return registeredQuestions.registeredQuestions;
};

const getAllQuestionsAsJSON = async (dataAccess) => {
    const registeredQuestionsBuffer = await dataAccess.getChainState(CHAIN_STATE_QUESTION);

    if (!registeredQuestionsBuffer) {
        return [];
    }

    const registeredQuestions = codec.decode(registeredQuestionSchema, registeredQuestionsBuffer);

    return codec.toJSON(registeredQuestionSchema, registeredQuestions).registeredQuestions;
};

const setAllQuestions = async (stateStore, questions) => {
    const registeredQuesions = {
        registeredQuestions: questions.sort((a, b) => a.id.compare(b.id)),
    };

    await stateStore.chain.set(
        CHAIN_STATE_QUESTION, 
        codec.encode(registeredQuestionSchema, registeredQuesions),
    );
};

module.exports = {
    registeredQuestionSchema, 
    CHAIN_STATE_QUESTION,
    createQuestion, 
    getAllQuestions, 
    getAllQuestionsAsJSON, 
    setAllQuestions
};


