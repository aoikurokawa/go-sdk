const { Application, configDevnet, genesisBlockDevnet, utils, HTTPAPIPlugin } = require("lisk-sdk");

const { QuizModule } = require("./quiz_module/index");
const { QuizAPIPlugin } = require("./quiz_api_plugin/index");

genesisBlockDevnet.header.timestamp = 1605699440;
genesisBlockDevnet.header.asset.accounts  = genesisBlockDevnet.header.asset.accounts.map(
    (a) => 
        utils.objects.mergeDeep({}, a, {
            quiz: {
                ownQuizs: [],
            },
        }),
);

const appConfig = utils.objects.mergeDeep({}, configDevnet, {
    label: 'quiz-app', 
    genesisConfig: {communityIdentifier: "QUIZ"}, 
    logger: {
        consoleLogLevel: 'info',
    },
});

const app = Application.defaultApplication(genesisBlockDevnet, appConfig);

app
    .run()
    .then(() => app.logger.info("App started..."))
    .catch((error) => {
        console.error("error", error);
    });

