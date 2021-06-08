const encodedTransactionSchema = {
    $id: 'quiz/encoded/transactions',
    type: 'object',
    required: ['transactions'],
    properties: {
        transactions: {
            type: 'array',
            fieldNumber: 1,
            items: {
                dataType: 'bytes',
            },
        },
    },
};

module.exports = { encodedTransactionSchema };