/*
=============================================================================
FreeFlowNetwork Module - Consortium System Tools

Copyright (c) 2025 Stepan Belopolsky (https://t.me/majworker)

You are permitted to integrate, use, and modify this software in your own
projects, provided that:
1. You do not sell, sublicense, or distribute this software or any derivatives
   for commercial gain.
2. You do not sublicense or sell the software to third parties.
3. The original copyright notice and this permission notice must be included
   in all copies or substantial portions of the software, including any files
   where this module is integrated.

All rights reserved. Resale, or sublicensing is strictly prohibited.
For commercial inquiries, contact the author.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
=============================================================================
 */


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