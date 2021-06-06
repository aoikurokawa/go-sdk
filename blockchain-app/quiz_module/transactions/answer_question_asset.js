const { BaseAsset } = require("lisk-sdk");
const { getAllQuestions, setAllQuestions } = require("../question");
const { AnswerQuestionSchema } = require("../schemas");

class AnswerQuestionAsset extends BaseAsset {
    name = "lisk/question/answer";
    id = 1;

    schema = AnswerQuestionAsset;

    async apply({ asset, stateStore, reducerHandler, transaction }) {
        const questions = await getAllQuestions(stateStore);
        const questionIndex = questions.findIndex((t) => t.id.equals(asset.questionId));

        if (questionIndex < 0) {
            throw new Error("Question id not found");
        }

        const question = questions[questionIndex];
        const questionOwner = await stateStore.account.get(question.ownerAddress);
        const questionOwnerAddress = questionOwner.address;

        const answererAddress = transacion.senderAddress;
        const answererAccount = await stateStore.account.get(answererAddress);

        if (question.answer === asset.answer) {
            // remove question from ownQuesitons
            const ownerQuestionsIndex = questionOwner.question.ownQuestions.findIndex((a) => a.equals(question.id));
            questionOwner.question.ownQuestions.splice(ownerQuestionsIndex, 1);
            await stateStore.account.set(questionOwnerAddress, questionOwner);
            // remove question that is correct answer
            questions.splice(questionIndex, 1);
            await setAllQuestions(stateStore, questions);

            // pay reward to answer account
            await reducerHandler.invoke("token:credit", {
                address: answererAddress, 
                amount: question.reward
            });
        }
    }
}

module.exports = AnswerQuestionAsset;

