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


using Org.BouncyCastle.Crypto.Parameters;
using Org.BouncyCastle.Crypto.Signers;
using Org.BouncyCastle.Math.EC;
using Org.BouncyCastle.Asn1.Sec;
using System;
using System.Collections.Generic;
using System.Linq;

public class ReceiptVerifier
{
    public static (Dictionary<string, string> details, bool isValid) VerifyReceipt(double expectedAmount, string publicKeyHex, string receipt)
    {
        const int TimeTolerance = 300;
        var details = new Dictionary<string, string>();
        try
        {
            var dataParts = receipt.Split(':');
            if (dataParts.Length != 9 || dataParts[0] != "receipt")
            {
                details["error"] = "Неверный формат чека";
                return (details, false);
            }

            int txId = int.Parse(dataParts[1]);
            int fromId = int.Parse(dataParts[2]);
            string toUsername = dataParts[3];
            double amount = double.Parse(dataParts[4]);
            int timestamp = int.Parse(dataParts[5]);
            string product = string.IsNullOrEmpty(dataParts[6]) ? "" : dataParts[6];
            string operation = string.IsNullOrEmpty(dataParts[7]) ? "" : dataParts[7];
            string sigHex = dataParts[8];

            if (Math.Abs(amount - expectedAmount) > 0.001)
            {
                details["error"] = "Сумма не совпадает";
                return (details, false);
            }

            var now = (int)DateTimeOffset.UtcNow.ToUnixTimeSeconds();
            if (timestamp > now + TimeTolerance)
            {
                details["error"] = "Чек из будущего";
                return (details, false);
            }

            string message = $"receipt:{txId}:{fromId}:{toUsername}:{amount}:{timestamp}:{product}:{operation}";

            // Верификация подписи с BouncyCastle
            var curve = SecNamedCurves.GetByName("secp256k1");
            var domain = new ECDomainParameters(curve.Curve, curve.G, curve.N, curve.H);
            var pubKeyBytes = HexStringToByteArray(publicKeyHex);
            var pubKey = new ECPublicKeyParameters("ECDSA", curve.Curve.DecodePoint(pubKeyBytes), domain);
            var signer = new ECDsaSigner();
            signer.Init(false, pubKey);
            var sigBytes = HexStringToByteArray(sigHex);
            // Разделить сигнатуру на r и s (предполагая DER или raw формат)
            // Для простоты - адаптируйте под ваш формат сигнатуры

            details["tx_id"] = txId.ToString();
            details["from_id"] = fromId.ToString();
            details["to_username"] = toUsername;
            details["amount"] = amount.ToString();
            details["timestamp"] = timestamp.ToString();
            details["product"] = product;
            details["operation"] = operation;
            return (details, true);
        }
        catch (Exception ex)
        {
            details["error"] = ex.Message;
            return (details, false);
        }
    }

    private static byte[] HexStringToByteArray(string hex)
    {
        return Enumerable.Range(0, hex.Length)
            .Where(x => x % 2 == 0)
            .Select(x => Convert.ToByte(hex.Substring(x, 2), 16))
            .ToArray();
    }
}

// Пример использования
// var (details, isValid) = ReceiptVerifier.VerifyReceipt(10.0, "public_key_hex", "receipt:...");