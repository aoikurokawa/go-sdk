const { BasePlugin } = require("lisk-sdk");
const pJSON = require("../package.json");

class QuizAPIPlugin extends BasePlugin {
    _server = undefined;
    _app = undefined;
    _channel = undefined;
    _db = undefined;
    _nodeInfo = undefined;

    static get alias() {
        return "QuizHttpApi";
    }

    static get info() {
        return {
            author: pJSON.author,
            version: pJSON.version,
            name: pJSON.name,
        };
    }

    get defaults() {
        return {};
    }

    get events() {
        return {};
    }

    get actions() {
        return {};
    }

}

module.exports = { QuizAPIPlugin };
