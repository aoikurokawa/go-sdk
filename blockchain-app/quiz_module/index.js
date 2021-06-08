const { BaseModule } = require("lisk-sdk");
const { questionAccountSchema } = require("./schemas");
const { getAllQuestionsAsJSON } = require("./question");

const CreateQueestionAsset = require("./transactions/create_question_asset");
const AnswerQuestionAsset = require("./transactions/answer_question_asset");

class QuizModule extends BaseModule {
    name = "question";
    id = 1024;
    accountSchema = questionAccountSchema;

    transactionAssets = [
        new CreateQueestionAsset(),
        new AnswerQuestionAsset(),
    ];

    actions = {
        getAllQuestions: async () => getAllQuestionsAsJSON(this._dataAccess),
    };
}

module.exports = { QuizModule };

