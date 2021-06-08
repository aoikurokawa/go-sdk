const { BaseAsset } = require("lisk-sdk");
const { createQuestionSchema } = require('../schemas');
const { createQuestion, getAllQuestions, setAllQuestions } = require("../question");

class CreateQuestionAsset extends BaseAsset {
    name = "createQuestion";
    id = 0;
    schema = createQuestionSchema;

    validate({ asset }) {
        if (asset.reward <= 0) {
            throw new Error("Reward is too low");
        }
    }

    async apply({ asset, stateStore, reducerHandler, transaction }) {
        const senderAddress = transaction.senderAddress;
        const senderAccount = await stateStore.account.get(senderAddress);
        const question = createQuestion({
            question: asset.question, 
            answer: asset.answer, 
            reward: asset.reward, 
            ownerAddress: senderAddress,
            nonce: transaction.nonce,
        });

        senderAccount.question.ownQuestion.push(question.id);
        await stateStore.account.set(senderAddress, senderAccount);

        await reducerHandler.invoke("token:debit", {
            address: senderAddress, 
            amount: asset.reward
        });

        const allQuestions = await getAllQuestions(stateStore);
        allQuestions.push(question);
        await setAllQuestions(stateStore, allQuestions);
    }
}

module.exports = CreateQuestionAsset;

