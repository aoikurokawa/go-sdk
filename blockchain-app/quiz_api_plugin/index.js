const express = require("express");
const cors = require("cors");
const { BasePlugin, codec } = require("lisk-sdk");
const pJSON = require("../package.json");
const { getDBInstance, getAllTransactions, saveTransactions, } = require("./db");

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

    async load(channel) {
        this._app = express();
        this._channel = channel;
        this._db = await getDBInstance();
        this._nodeInfo = await this._channel.invoke("app:getNodeInfo");

        this._app.use(cors({ origin: "*", methods: ["GET", "POST", "PUT"] }));
        this._app.use(express.json());

        // this._app.get("/api/quiz", async (_req, res) => {
        //     const quizes = await this._channel.invoke("quiz/getAllQuiz");
        //     const data = await Promise.all(quizes.map(async quiz => {
        //         const dbKey = `${quiz.name}`;
        //         let 
        //     }))
        // })

        this._app.get("/api/transactions", async (_req, res) => {
            const transactions = await getAllTransactions(this._db, this.schemas);
            const data = transactions.map(trx => {
                const module = this._nodeInfo.registeredModules.find(m => m.id === trx.moduleID);
                const asset = module.transactionAssets.find(a => a.id === trx.id);
                return {
                    ...trx,
                    ...trx.asset,
                    moduleName: module.name,
                    assetName: asset.name,
                };
            });
            res.json({ data });
        });
        this._subscribeToChannel();
        this._server = this._app.listen(8080, "0.0.0.0");
    }

    _subscribeToChannel() {
        this._channel.subscribe('app:block:new', async (data) => {
            const { block } = data;
            const { payload } = codec.decode(
                this.schemas.block,
                Buffer.from(block, 'hex'),
            );
            if (payload.length > 0) {
                await saveTransactions(this._db, payload);
                const decodedBlock = this.codec.decodeBlock(block);
            }
        });
    }

    async unload() {
        await new Promise((resolve, reject) => {
            this._server.close((err) => {
                if (err) {
                    reject(err);
                    return;
                }
                resolve();
            });
        });

        await this._db.close();
    }
}

module.exports = { QuizAPIPlugin };
