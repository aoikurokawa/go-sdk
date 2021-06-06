const { Application, configDevnet, genesisBlockDevnet, utils } = require("lisk-sdk");

const app = Application.defaultApplication(genesisBlockDevnet, configDevnet);

app
.run()
.then(() => app.logger.info("App started..."))
.catch((error) => {
    console.error("error", error);
    process.exit(1);
});

