const { codec, cryptography } = require("lisk-sdk");

const { registeredQuestionSchema } = require("./schemas");

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


