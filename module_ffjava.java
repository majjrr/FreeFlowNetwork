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


import org.bouncycastle.asn1.sec.SECNamedCurves;
import org.bouncycastle.asn1.x9.X9ECParameters;
import org.bouncycastle.crypto.params.ECDomainParameters;
import org.bouncycastle.crypto.params.ECPublicKeyParameters;
import org.bouncycastle.crypto.signers.ECDSASigner;
import org.bouncycastle.math.ec.ECPoint;

import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;

public class ReceiptVerifier {
    public static Map<String, Object> verifyReceipt(double expectedAmount, String publicKeyHex, String receipt) {
        Map<String, Object> result = new HashMap<>();
        result.put("isValid", false);
        Map<String, String> details = new HashMap<>();

        final int TIME_TOLERANCE = 300;
        try {
            String[] dataParts = receipt.split(":");
            if (dataParts.length != 9 || !dataParts[0].equals("receipt")) {
                details.put("error", "Неверный формат чека");
                result.put("details", details);
                return result;
            }

            int txId = Integer.parseInt(dataParts[1]);
            int fromId = Integer.parseInt(dataParts[2]);
            String toUsername = dataParts[3];
            double amount = Double.parseDouble(dataParts[4]);
            int timestamp = Integer.parseInt(dataParts[5]);
            String product = dataParts[6].isEmpty() ? "" : dataParts[6];
            String operation = dataParts[7].isEmpty() ? "" : dataParts[7];
            String sigHex = dataParts[8];

            if (Math.abs(amount - expectedAmount) > 0.001) {
                details.put("error", "Сумма не совпадает");
                result.put("details", details);
                return result;
            }

            long now = System.currentTimeMillis() / 1000;
            if (timestamp > now + TIME_TOLERANCE) {
                details.put("error", "Чек из будущего");
                result.put("details", details);
                return result;
            }

            String message = "receipt:" + txId + ":" + fromId + ":" + toUsername + ":" + amount + ":" + timestamp + ":" + product + ":" + operation;

            // Верификация подписи с BouncyCastle
            X9ECParameters params = SECNamedCurves.getByName("secp256k1");
            ECDomainParameters domain = new ECDomainParameters(params.getCurve(), params.getG(), params.getN(), params.getH());
            byte[] pubKeyBytes = hexStringToByteArray(publicKeyHex);
            ECPoint point = params.getCurve().decodePoint(pubKeyBytes);
            ECPublicKeyParameters pubKey = new ECPublicKeyParameters(point, domain);
            ECDSASigner signer = new ECDSASigner();
            signer.init(false, pubKey);
            byte[] sigBytes = hexStringToByteArray(sigHex);
            // Разделить на r и s (адаптируйте)
            BigInteger r = new BigInteger(1, sigBytes, 0, sigBytes.length / 2);
            BigInteger s = new BigInteger(1, sigBytes, sigBytes.length / 2, sigBytes.length / 2);
            if (signer.verifySignature(message.getBytes(), r, s)) {
                details.put("tx_id", Integer.toString(txId));
                details.put("from_id", Integer.toString(fromId));
                details.put("to_username", toUsername);
                details.put("amount", Double.toString(amount));
                details.put("timestamp", Integer.toString(timestamp));
                details.put("product", product);
                details.put("operation", operation);
                result.put("details", details);
                result.put("isValid", true);
            } else {
                details.put("error", "Неверная подпись");
                result.put("details", details);
            }
        } catch (Exception ex) {
            details.put("error", ex.getMessage());
            result.put("details", details);
        }
        return result;
    }

    private static byte[] hexStringToByteArray(String hex) {
        int len = hex.length();
        byte[] data = new byte[len / 2];
        for (int i = 0; i < len; i += 2) {
            data[i / 2] = (byte) ((Character.digit(hex.charAt(i), 16) << 4) + Character.digit(hex.charAt(i + 1), 16));
        }
        return data;
    }
}

// Пример использования
// Map<String, Object> result = ReceiptVerifier.verifyReceipt(10.0, "public_key_hex", "receipt:...");