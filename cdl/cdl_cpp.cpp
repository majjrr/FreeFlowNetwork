#include <iostream>
#include <string>
#include <iomanip>
#include <sstream>
#include <regex>  // Для замены и валидации

std::string createDeepLink(const std::string& botUsername, std::string recipient, double amount, const std::string& product) {
    // Убрать @
    if (recipient.find('@') == 0) {
        recipient = recipient.substr(1);
    }

    // Валидация
    if (amount <= 0.0 || recipient.length() > 32 || product.length() > 20 || product.find(' ') != std::string::npos) {
        std::cerr << "Неверные параметры для deep link" << std::endl;
        return "";
    }
    // Заглушка для мата (реализуйте filterProfanity)
    if (!filterProfanity(recipient) || !filterProfanity(product)) {
        std::cerr << "Недопустимые слова в параметрах" << std::endl;
        return "";
    }

    // Форматирование amount (2 знака после запятой)
    std::ostringstream oss;
    oss << std::fixed << std::setprecision(2) << amount;
    std::string amountStr = oss.str();
    size_t dotPos = amountStr.find('.');
    if (dotPos != std::string::npos) {
        amountStr.replace(dotPos, 1, "_");  // . → _
    }

    // Параметр start
    std::string payParam = "pay_to_" + recipient + "_" + amountStr + "_" + product;
    if (payParam.length() > 64) {
        std::cerr << "Параметр слишком длинный: " << payParam.length() << " > 64" << std::endl;
        return "";
    }

    // Ссылка
    std::string deepLink = "https://t.me/" + botUsername + "?start=" + payParam;
    std::cout << "Создана deep link: " << deepLink << std::endl;
    return deepLink;
}

bool filterProfanity(const std::string& str) {
    // Реализуйте: return std::regex_search(str, std::regex("badword")) == false;
    return true;  // Заглушка
}

// Пример
int main() {
    std::string link = createDeepLink("FreeFlowNetwork_bot", "majworker", 0.10, "9999A");
    std::cout << link << std::endl;  // https://t.me/FreeFlowNetwork_bot?start=pay_to_majworker_0_10_9999A
    return 0;
}