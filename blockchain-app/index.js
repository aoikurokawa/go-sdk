const { Application, configDevnet, genesisBlockDevnet, utils, HTTPAPIPlugin } = require("lisk-sdk");

const { QuizModule } = require("./quiz_module");
const { QuizAPIPlugin } = require("./quiz_api_plugin");

genesisBlockDevnet.header.timestamp = 1605699440;
genesisBlockDevnet.header.asset.accounts = genesisBlockDevnet.header.asset.accounts.map(
    (account) =>
        utils.objects.mergeDeep({}, account, {
            quiz: {
                ownQuizzes: [],
            },
        }),
);

const appConfig = utils.objects.mergeDeep({}, configDevnet, {
    label: 'quiz-app',
    genesisConfig: { communityIdentifier: 'QUIZ' },
    logger: {
        consoleLogLevel: 'info',
    },
});

const app = Application.defaultApplication(genesisBlockDevnet, appConfig);

app.registerModule(QuizModule);
app.registerPlugin(HTTPAPIPlugin);
app.registerPlugin(QuizAPIPlugin);

app
    .run()
    .then(() => console.info("Quiz appchain running..."))
    .catch(console.error);

