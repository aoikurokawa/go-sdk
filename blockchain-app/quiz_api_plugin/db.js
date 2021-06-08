const fs_extra = require("fs-extra");
const os = require("os");
const path = require("path");
const { cryptography, codec, db } = require("lisk-sdk");

const DB_KEY_TRANSACTIONS = 'quiz:transactions';
const CREATEQUIZ_ASSET_ID = 0;


