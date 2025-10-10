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


#include <secp256k1.h>
#include <secp256k1_recovery.h>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <ctime>
#include <iomanip>
#include <stdexcept>

std::pair<std::map<std::string, std::string>, bool> verify_receipt(double expected_amount, const std::string& public_key_hex, const std::string& receipt) {
    const int TIME_TOLERANCE = 300;
    std::map<std::string, std::string> details;
    try {
        std::vector<std::string> data_parts;
        std::stringstream ss(receipt);
        std::string part;
        while (std::getline(ss, part, ':')) {
            data_parts.push_back(part);
        }
        if (data_parts.size() != 9 || data_parts[0] != "receipt") {
            details["error"] = "Неверный формат чека";
            return {details, false};
        }

        int tx_id = std::stoi(data_parts[1]);
        int from_id = std::stoi(data_parts[2]);
        std::string to_username = data_parts[3];
        double amount = std::stod(data_parts[4]);
        int timestamp = std::stoi(data_parts[5]);
        std::string product = data_parts[6].empty() ? "" : data_parts[6];
        std::string operation = data_parts[7].empty() ? "" : data_parts[7];
        std::string sig_hex = data_parts[8];

        if (std::abs(amount - expected_amount) > 0.001) {
            details["error"] = "Сумма не совпадает";
            return {details, false};
        }

        time_t now = time(nullptr);
        if (timestamp > now + TIME_TOLERANCE) {
            details["error"] = "Чек из будущего";
            return {details, false};
        }

        std::stringstream msg_ss;
        msg_ss << "receipt:" << tx_id << ":" << from_id << ":" << to_username << ":" << std::fixed << std::setprecision(1) << amount << ":" << timestamp << ":" << product << ":" << operation;
        std::string message = msg_ss.str();

        // Верификация подписи (требует адаптации под libsecp256k1)
        // Здесь placeholder, так как libsecp256k1 требует детальной реализации
        // Для полной работы используйте secp256k1_ecdsa_verify_sig

        details["tx_id"] = std::to_string(tx_id);
        details["from_id"] = std::to_string(from_id);
        details["to_username"] = to_username;
        details["amount"] = std::to_string(amount);
        details["timestamp"] = std::to_string(timestamp);
        details["product"] = product;
        details["operation"] = operation;
        return {details, true};
    } catch (const std::exception& ex) {
        details["error"] = ex.what();
        return {details, false};
    }
}

// Пример использования
// auto [details, is_valid] = verify_receipt(10.0, "public_key_hex", "receipt:...");