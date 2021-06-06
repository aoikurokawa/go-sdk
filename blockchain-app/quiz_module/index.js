const { BaseModule } = require("lisk-sdk");
const { QuestionAccountSchema } = require("./schemas");

class QuizModule extends BaseModule {
    name = "question";
    id = 1024;
    accountSchema = QuestionAccountSchema;
}

module.exports = QuizModule;

