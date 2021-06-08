const fs_extra = require("fs-extra");
const os = require("os");
const path = require("path");
const { cryptography, codec, db } = require("lisk-sdk");
const { encodedTransactionSchema } = require("./schemas");

const DB_KEY_TRANSACTIONS = 'quiz:transactions';
const CREATEQUIZ_ASSET_ID = 0;

const getDBInstance = async (dataPath = '~/.lisk/quiz-app/', dbName = 'quiz-plugin.db') => {
    const dirPath = path.join(dataPath.replace('~', os.homedir()), 'plugins/data', dbName);
    await fs_extra.ensureDir(dirPath);
    return new db.KVStore(dirPath);
};

const saveTransactions = async (db, payload) => {
    const savedTransactions = await getTransactions(db);
    const transactions = [...savedTransactions, ...payload];
    const encodedTransactions = codec.encode(encodedTransactionSchema, { transactions });
    await db.put(DB_KEY_TRANSACTIONS, encodedTransactions);
};

const getTransactions = async (db) => {
    try {
        const encodedTransactions = await db.get(DB_KEY_TRANSACTIONS);
        const { transactions } = codec.decode(encodedTransactionSchema, encodedTransactions);
        return transactions;
    } catch (error) {
        return [];
    }
}

const getAllTransactions = async (db, registeredSchema) => {
    const savedTransactions = await getTransactions(db);
    const transactions = [];
    for (const trx of savedTransactions) {
        transactions.push(decodeTransaction(trx, registeredSchema));
    }
    return transactions;
}

const decodeTransaction = (encodedTransaction, registeredSchema) => {
    const transaction = codec.decode(registeredSchema.transaction, encodedTransaction);
    const assetSchema = getTransactionAssetSchema(transaction, registeredSchema);
    const asset = codec.decode(assetSchema, transaction.asset);
    const id = cryptography.hash(encodedTransaction);
    return {
        ...codec.toJSON(registeredSchema.transaction, transaction), 
        asset: codec.toJSON(assetSchema, asset),
        id: id.toString('hex'), 
    };
};

const getTransactionAssetSchema = (transaction, registeredSchema) => {
    const txAssetSchema = registeredSchema.transactionAssets.find(
        assetSchema => 
            assetSchema.moduleID === transaction.moduleID && assetSchema.assetID === transaction.assetID,
    );
    if (!txAssetSchema) {
        throw new Error(
            `ModuleID: ${transaction.moduleID} AssetID: ${transaction.assetID} is not registered`,
        );
    }
    return txAssetSchema.schema;
};

module.exports = {
    getDBInstance, 
    getAllTransactions, 
    getTransactions, 
    saveTransactions,
};
