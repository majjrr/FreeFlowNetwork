# =============================================================================
# FreeFlowNetwork Module - Consortium System Tools
# 
# Copyright (c) 2025 Stepan Belopolsky (https://t.me/majworker)
# 
# You are permitted to integrate, use, and modify this software in your own
# projects, provided that:
# 1. You do not sell, sublicense, or distribute this software or any derivatives
#    for commercial gain.
# 2. You do not sublicense or sell the software to third parties.
# 3. The original copyright notice and this permission notice must be included
#    in all copies or substantial portions of the software, including any files
#    where this module is integrated.
# 
# All rights reserved. Resale, or sublicensing is strictly prohibited.
# For commercial inquiries, contact the author.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =============================================================================


import ecdsa
import time

def verify_receipt(expected_amount: float, public_key_hex: str, receipt: str) -> (dict, bool):
    TIME_TOLERANCE = 300
    try:
        data_parts = receipt.split(":")
        if len(data_parts) != 9 or data_parts[0] != "receipt":
            return {"error": "Неверный формат чека"}, False

        tx_id, from_id, to_username, amount, timestamp, product, operation, sig_hex = data_parts[1:]
        amount = float(amount)
        timestamp = int(timestamp)
        from_id = int(from_id)
        tx_id = int(tx_id)
        product = product if product else ''
        operation = operation if operation else ''

        if abs(amount - expected_amount) > 0.001:
            return {"error": f"Сумма не совпадает: {amount} != {expected_amount}"}, False

        if timestamp > time.time() + TIME_TOLERANCE:
            return {"error": "Чек из будущего"}, False

        message = f"receipt:{tx_id}:{from_id}:{to_username}:{amount}:{timestamp}:{product}:{operation}".encode()
        vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key_hex), curve=ecdsa.SECP256k1)
        if vk.verify(bytes.fromhex(sig_hex), message):
            details = {
                "tx_id": tx_id,
                "from_id": from_id,
                "to_username": to_username,
                "amount": amount,
                "timestamp": timestamp,
                "product": product,
                "operation": operation
            }
            return details, True
        else:
            return {"error": "Неверная подпись"}, False
    except Exception as ex:
        return {"error": str(ex)}, False

# Пример использования
# BOT_PUBLIC_KEY_HEX = "your_key_here"
# receipt = "receipt:1:123:user:10.0:1727600000:product:operation:sig_hex"
# details, is_valid = verify_receipt(10.0, BOT_PUBLIC_KEY_HEX, receipt)
# print(details, is_valid)