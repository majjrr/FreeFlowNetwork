const elliptic = require('elliptic');
const EC = elliptic.ec;
const ec = new EC('secp256k1');

function verifyReceipt(expectedAmount, publicKeyHex, receipt) {
    const TIME_TOLERANCE = 300;
    const details = {};
    try {
        const dataParts = receipt.split(':');
        if (dataParts.length !== 9 || dataParts[0] !== 'receipt') {
            details.error = 'Неверный формат чека';
            return [details, false];
        }

        const txId = parseInt(dataParts[1]);
        const fromId = parseInt(dataParts[2]);
        const toUsername = dataParts[3];
        const amount = parseFloat(dataParts[4]);
        const timestamp = parseInt(dataParts[5]);
        const product = dataParts[6] || '';
        const operation = dataParts[7] || '';
        const sigHex = dataParts[8];

        if (Math.abs(amount - expectedAmount) > 0.001) {
            details.error = 'Сумма не совпадает';
            return [details, false];
        }

        const now = Math.floor(Date.now() / 1000);
        if (timestamp > now + TIME_TOLERANCE) {
            details.error = 'Чек из будущего';
            return [details, false];
        }

        const message = `receipt:${txId}:${fromId}:${toUsername}:${amount}:${timestamp}:${product}:${operation}`;

        // Верификация подписи
        const key = ec.keyFromPublic(publicKeyHex, 'hex');
        const sig = { r: sigHex.slice(0, 64), s: sigHex.slice(64) }; // Адаптируйте под raw формат
        if (key.verify(message, sig)) {
            details.tx_id = txId;
            details.from_id = fromId;
            details.to_username = toUsername;
            details.amount = amount;
            details.timestamp = timestamp;
            details.product = product;
            details.operation = operation;
            return [details, true];
        } else {
            details.error = 'Неверная подпись';
            return [details, false];
        }
    } catch (ex) {
        details.error = ex.message;
        return [details, false];
    }
}

// Пример использования
// const [details, isValid] = verifyReceipt(10.0, 'public_key_hex', 'receipt:...');