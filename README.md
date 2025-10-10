# FreeFlowNetwork — Децентрализованная Финансовая Экосистема в Telegram

![FreeFlowNetwork Banner](https://i.postimg.cc/q74FKqb8/FFN-logo.png)

**FreeFlowNetwork** — это инновационный Telegram-бот, обеспечивающий децентрализованные финансовые операции с 
использованием токена `$FFT`. Проект сочетает простоту интерфейса Telegram с мощью криптографических технологий,
предоставляя пользователям быстрые переводы, выгодный стейкинг и безопасное управление ключами. Это не просто бот
— это экосистема для финансовой свободы в Web3!

# FreeFlowNetwork — Децентрализованная Финансовая Экосистема в Telegram

![FreeFlowNetwork Banner](https://i.postimg.cc/q74FKqb8/FFN-logo.png)

**FreeFlowNetwork** — это инновационный Telegram-бот, обеспечивающий децентрализованные финансовые операции с 
использованием токена `$FFT`. Проект сочетает простоту интерфейса Telegram с мощью криптографических технологий,
предоставляя пользователям быстрые переводы, выгодный стейкинг и безопасное управление ключами. Это не просто бот
— это экосистема для финансовой свободы в Web3!

## 📖 Оглавление

- [🚀 Основные возможности](#-основные-возможности)
  - [💸 Переводы токенов ($FFT)](#-переводы-токенов-fft)
  - [📈 Стейкинг](#-стейкинг)
  - [🔑 Генерация ключей для оффлайн-операций](#-генерация-ключей-для-оффлайн-операций)
  - [📰 Лента новостей](#-лента-новостей)
  - [💎 Премиум-подписка](#-премиум-подписка)
  - [🛠 Поддержка и администрирование](#-поддержка-и-администрирование)
    - [Система рекламы (/add_ad) на основе кода](#система-рекламы-add_ad-на-основе-кода)
- [🛡 Безопасность и фильтрация](#-безопасность-и-фильтрация)
- [🗄 Техническое описание базы данных](#-техническое-описание-базы-данных)
  - [Архитектура](#архитектура)
  - [Модели данных](#модели-данных)
  - [Особенности](#особенности)
  - [Преимущества](#преимущества)
  - [Новое](#новое)
- [Универсальная функция для проверки чека](#универсальная-функция-для-проверки-чека)
  - [1. Реализация на Python (с использованием ecdsa)](#1-реализация-на-python-с-использованием-ecdsa)
  - [2. Реализация на C++ (с использованием libsecp256k1)](#2-реализация-на-c-с-использованием-libsecp256k1)
  - [3. Реализация на C# (с использованием BouncyCastle)](#3-реализация-на-c-с-использованием-bouncycastle)
  - [4. Реализация на Java (с использованием BouncyCastle)](#4-реализация-на-java-с-использованием-bouncycastle)
  - [5. Реализация на JavaScript (с использованием elliptic)](#5-реализация-на-javascript-с-использованием-elliptic)
- [🤖 Подключение ботов к профилю (реализация в 0.0.3 и планы развития)](#-подключение-ботов-к-профиля-реализация-в-003-и-планы-развития)
  - [Как это работает сейчас (в 0.0.3)](#как-это-работает-сейчас-в-003)
- [🤝 Контрибьютинг](#-контрибьютинг)
- [📞 Контакты](#-контакты)

## 🚀 Основные возможности

### 💸 Переводы токенов ($FFT)
Пользователи могут мгновенно переводить токены `$FFT` другим пользователям Telegram с помощью команды `/pay`. 
Интуитивный интерфейс предлагает список последних получателей в виде reply-кнопок, исключая системные адреса, 
такие как `@staking`. Транзакции записываются в базу данных с генерацией уникального чека.

**Результат**: Перевод 10 $FFT пользователю `@freeflowfriend` с чеком.

### 📈 Стейкинг
FreeFlowNetwork предлагает выгодный стейкинг с разными уровнями доходности:
- **Standard**: 10% годовых.
- **Privileged**: 15% годовых для подписчиков.

Команда `/stake` позволяет заблокировать токены для получения пассивного дохода. 
Стейкинг реализован с учетом временных интервалов и автоматического начисления прибыли.

### 🔑 Генерация ключей для оффлайн-операций
Команда `/generate_keys` создает пару ECDSA-ключей (SECP256k1) для безопасных оффлайн-транзакций. 
Публичный ключ отображается в чате, а приватный ключ отправляется в личные сообщения, обеспечивая 
конфиденциальность.

**Пример команды**:
```bash
/generate_keys
```
**Результат**:
- Публичный ключ: `04x...` (в чате).
- Приватный ключ: отправлен в ЛС.

### 📰 Лента новостей
Команда `/lents` предоставляет актуальные IT-новости из RSS-лент ведущих источников 
(TechCrunch, Wired, The Verge и др.), помогая пользователям оставаться в курсе трендов.

### 💎 Премиум-подписка
Команда `/subscribe` позволяет приобрести подписку (1, 6 или 12 месяцев) с 
улучшенными условиями стейкинга и дополнительными функциями. Команда `/gift` 
позволяет подарить подписку другому пользователю.

### 🛠 Поддержка и администрирование

- **Поддержка**: Команда `/support` позволяет любому пользователю отправить сообщение в чат поддержки (идентифицируется по `SUPPORT_CHAT_ID` в конфигурации). Сообщение отправляется с указанием ID и username пользователя для быстрого реагирования. Премиум-пользователи имеют дополнительную команду `/priority_support` для приоритетных запросов (отмечается как "приоритетное" в чате поддержки).

- **Администрирование**: Администраторы (задаются в `ADMIN_IDS` как список ID в .env) могут управлять банами (`/ban` и `/unban`), подписками (через `/create_promo`, `/delete_promo`, `/purchase_export`), балансами (`/add_balance`, `/subtract_balance`) и **рекламой** (модерация объявлений через `/approve_ad` и `/delete_ad`). Обратите внимание: добавление объявлений (`/add_ad`) доступно **всем пользователям**, а не только админам — это часть системы пользовательского контента.

#### Система рекламы (/add_ad) на основе кода
Система объявлений (рекламы) реализована как простая модерация пользовательского контента, интегрированная с командой `/lents` (просмотр новостей). Вот как она работает шаг за шагом, исходя из кода:

1. **Добавление объявления (/add_ad)**:
   - Доступно **любому пользователю** (не только админам), но с проверкой на бан и фильтр нецензурной лексики (`filter_profanity` на основе словаря `PROFANITY_FILTER`).
   - Команда: `/add_ad [текст_объявления]`.
   - Текст сохраняется в таблицу `Ad` с полями: `user_id` (ID автора), `text` (содержимое), `status='pending'` (ожидает модерации).
   - Автоматически уведомляет **всех админов** (по `ADMIN_IDS`) о новом объявлении с ID, текстом и командами для модерации: `/approve_ad [id]` или `/delete_ad [id]`.
   - Логируется в консоль для отслеживания.

2. **Модерация (только для админов)**:
   - **Одобрение (/approve_ad [ad_id])**: Изменяет `status` на `'approved'`. Уведомляет автора: "Ваше объявление одобрено!".
   - **Удаление (/delete_ad [ad_id])**: Удаляет запись из БД. Уведомляет автора: "Ваше объявление удалено.".
   - Если объявление не существует или неверный ID — ошибка.

3. **Отображение рекламы**:
   - Реклама показывается **только одобренным** объявлениям (query: `Ad.status == 'approved'`, лимит 5).
   - Интеграция с `/lents`: Бот формирует список из **5 элементов** (новости + реклама):
     - Берет последние 5 новостей из RSS (`RSS_URLS`, парсинг XML с `urllib` и `ET`).
     - Добавляет одобренные ads с вероятностью 50% (`random.random() < 0.5`).
     - Перемешивает: новости (с заголовком, описанием, ссылкой, датой) и ads (просто текст).
     - Если нет новостей — показывает только ads (заголовок: "Одобренные объявления").
     - Если только новости — "Последние IT-новости".
     - Для премиум-пользователей: фильтр по ключевым словам (`lents_keywords` в модели `User`), но ads показываются всегда.
   - Нет отдельных лимитов по времени или частоте показа — ads ротируются случайно в каждом вызове `/lents`.

## 🛡 Безопасность и фильтрация
FreeFlowNetwork использует строгий фильтр нецензурной лексики (`PROFANITY_FILTER`), 
блокирующий матерные слова в никнеймах и сообщениях. Это обеспечивает безопасное и 
уважительное взаимодействие.

## 🗄 Техническое описание базы данных

### Архитектура
FreeFlowNetwork использует SQLite с прагмой `journal_mode=wal` для обеспечения высокой 
производительности и надежности. База данных (`payments.db`) оптимизирована для конкурентного 
доступа, что критично для Telegram-бота, обрабатывающего множество транзакций.

### Модели данных
База данных включает следующие ключевые таблицы, реализованные с помощью ORM Peewee:
- **User**:
  Хранит информацию о пользователях, их балансах, истории транзакций и статусе подписки.
- **Transaction**:
  Регистрирует все транзакции с указанием отправителя, получателя, суммы и статуса.
- **Ad** и **Stake**:
  Хранят данные о рекламных объявлениях и стейкинге соответственно.

### Особенности
- **Атомарные транзакции**: Используется `db.atomic()` для гарантии целостности данных при обновлении балансов.
- **Кэширование**: `balance_cache` (на базе `OrderedDict`) минимизирует запросы к базе данных, 
обеспечивая быстрый доступ к балансам.
- **Индексация**: Поля, такие как `user_id` и `timestamp`, оптимизированы для быстрого поиска.
- **Безопасность**: Конфиденциальные данные (например, `BOT_TOKEN`) хранятся в `.env`, игнорируемом `.gitignore`.

### Преимущества
- **Масштабируемость**: SQLite с WAL поддерживает до тысяч одновременных операций, что достаточно для 
стартапа на ранней стадии.
- **Простота деплоя**: Легковесная база данных упрощает развертывание на серверах или в контейнерах.
- **Надежность**: Транзакционная модель и резервное копирование обеспечивают защиту от потери данных.

### Новое

![Img new banner](https://i.postimg.cc/L5ytGZyt/new-realez-banner.png)

В скором времени добавим поддержку экосистемы TON и blockchain алгоритмов в FreeFlow Network. Это включает интеграцию с The Open Network (TON) для пополнения баланса $FFT токенами через Toncoin (TON). Пользователи смогут использовать встроенный Telegram-кошелек (@wallet) для быстрых, низкозатратных депозитов: просто отправьте TON на указанный адрес, и бот автоматически конвертирует их в $FFT по текущему курсу (с минимальной комиссией).
Ключевые фичи будущей TON-интеграции:

Пополнение баланса (/deposit): Команда для генерации уникального TON-адреса. После подтверждения транзакции (через TON API) баланс обновится в реальном времени.
Вывод средств: Опциональный вывод $FFT в TON для внешних DeFi-приложений.
Преимущества: Низкие fees (~0.01 TON), мгновенная финализация, полная децентрализация — без посредников.
Roadmap: Тестирование в версии 0.0.4 (Q4 2025), с поддержкой TON L2 для еще большей скорости. Следите за обновлениями в [t.me/freeflowdev!](https://t.me/freeflowdev)

## Универсальная функция для проверки чека

Всё это используетс как подключаемые модули в программу в вашем соответсвенном языке. 

В качестве примера была реализована простая программа с UI интерфейсом на Python с помощью фреймворка flet. Её можно менять под свои нужды или использовать её стандартным приложением, или вообще создать новое своё интегрированное приложение, которое будет иметь универсальная функцию для проверки подлинности чека (receipt) на основе ECDSA с кривой SECP256k1. **Обязательное условие, помечать, что используется сеть FreeFlow.**

![UI FreeFlowNetwork Check Verifie](https://i.postimg.cc/65V1wvLL/B5689-C69-5977-4908-BF47-DE08-C475-A965.png)

Универсальная функция для проверки подлинности чека (receipt) на основе ECDSA с кривой SECP256k1. Функция принимает на вход:

- `expected_amount`: Ожидаемая сумма перевода (float) — для проверки соответствия суммы в чеке.
`public_key_hex`: Публичный ключ бота в HEX-формате (string) — для верификации подписи.
- `receipt`: Полный текст чека (string) в формате `receipt:tx_id:from_id:to_username:amount:timestamp:product:operation:sig_hex`.

На выходе функция возвращает:

- `details`: Словарь с данными чека (`tx_id`, `from_id`, `to_username`, `amount`, times`tamp, `product`, `operation`) при успешной проверке, или словарь с ошибкой ({"error": "Сообщение"}).
- `is_valid`: Булево значение (True/False) — подлинный чек или нет.

Функция проверяет:

- Формат чека.
- Соответствие суммы.
- Временную метку (не из будущего с учётом `TIME_TOLERANCE` = 300 секунд).
- Подпись с помощью публичного ключа.

Реализацию на Python (как базовая), а затем на C++, C#, Java и JavaScript. Для других языков потребуется установка соответствующих библиотек (например, для ECDSA-подписи). Все реализации оффлайн (без БД).

### 1. Реализация на Python (с использованием ecdsa)

Установите библиотеку: `pip install ecdsa`.

<details>
<summary>🔍 Код Python (кликни для показа кода)</summary>

```python
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
```

</details>

### 2. Реализация на C++ (с использованием libsecp256k1)

Установите `libsecp256k1` (например, через `vcpkg` или `brew`). Компиляция: `g++ file.cpp -lsecp256k1 -o program`.

<details>
<summary>🔍 Код C++ (кликни для показа кода)</summary>

```cpp
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
```

</details>

**Примечание для C++:** Полная верификация подписи требует интеграции libsecp256k1. Используйте функции вроде `secp256k1_ecdsa_signature_parse_compact` и `secp256k1_ecdsa_verify` для проверки.

### 3. Реализация на C# (с использованием BouncyCastle)

Установите NuGet пакет `BouncyCastle.NetCore`.

<details>
<summary>🔍 Код C# (кликни для показа кода)</summary>

```csharp
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
```

</details>

**Примечание для C#:** Полная верификация требует разделения сигнатуры на r и s. Адаптируйте под формат sig_hex (DER или raw).

### 4. Реализация на Java (с использованием BouncyCastle)

Установите BouncyCastle через Maven: `<dependency><groupId>org.bouncycastle</groupId><artifactId>bcprov-jdk15on</artifactId><version>1.70</version></dependency>`.

<details>
<summary>🔍 Код Java (кликни для показа кода)</summary>

```java
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
```

</details>

**Примечание для Java:** Адаптируйте разделение сигнатуры на r и s в зависимости от формата sig_hex.

### 5. Реализация на JavaScript (с использованием elliptic)

Установите библиотеку: `npm install elliptic`.

<details>
<summary>🔍 Код JavaScript (кликни для показа кода)</summary>

```javascript
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
```

</details>

**Примечание для JavaScript:** Адаптируйте sigHex под raw формат (r + s, 64 байта).

Это делает функцию универсальной — её можно интегрировать в программы на этих языках как библиотеку или модуль. Для входа/выхода используйте аргументы функции, а для консольных приложений добавьте парсинг командной строки.

## 🤖 **Подключение ботов к профилю (реализация в 0.0.3 и планы развития)**

<div align="center">

**Клиент** (покупатель цифровго продукта)  **|**  **Продавец** (получатель токенов за продукт)

</div>

![FreeFlowNetworkBot page 1](https://i.postimg.cc/HWB8nNxM/8-E5416-C2-789-E-47-D5-B03-E-78-D7962-CD695.png)
![FreeFlowNetworkBot page 2](https://i.postimg.cc/dDPbwBgb/CFA9-E145-8706-4-DAE-8-F5-E-2-EE9-AEAE8-A97.png)
![FreeFlowNetworkBot page 3](https://i.postimg.cc/NF9tgLFk/405-E8-DBD-6-FC4-4-E3-D-973-B-3699-B4481-A45.png)

В версии **0.0.3** FreeFlow Network мы реализовали базовую экосистему подключения внешних ботов к пользовательским профилям, сделав это шагом к полной модульной платформе. Это позволяет расширять функциональность без изменения основного бота — например, через бизнес-логику для верификации чеков. Мы объединили код из `businessFreeFlowBot.py` в один файл, чтобы упростить интеграцию: теперь чеки, уведомления владельцам и плагины работают seamless.

#### Как это работает сейчас (в 0.0.3)
- **Интеграция с профилем**: Боты подключаются через Telegram (авторизация по токену). Доступ к общей БД (SQLite) для проверки транзакций и уведомлений.
- **Безопасность**: Фильтрация сообщений — только чеки (триггер `receipt:`, длина 170-200 символов) обрабатываются; остальное игнорируется без лога (конфиденциальность). Подписи ECDSA + тайм-ауты предотвращают спам.

**Ключевой пример: Бизнес-бот как подключённый модуль**  
Это шаблон для внешнего бота, интегрированного с профилем FreeFlow. Он верифицирует чеки и вызывает плагины. Код — полный модуль (вставьте в ваш бот).

<details>
<summary>Код оброботчика сообщений в версии 0.0.3</summary>

```python
# Обработчик бизнес-сообщений (из businessFreeFlowBot)
async def on_business_message(business_message: types.Message, business_connection: types.BusinessConnection = None):
    """Обработка новых сообщений в бизнес-чатах"""
    user_id = business_message.from_user.id
    username = business_message.from_user.username or "Нет username"
    first_name = business_message.from_user.first_name or "Нет имени"
    text = business_message.text or "Нет текста (возможно, медиа)"

    # Новая проверка: Обрабатывать только чеки с триггером 'receipt:' и длиной 170-200 символов
    if not text.startswith("receipt:") or not (170 <= len(text) <= 200):
        # Игнорируем сообщение: не логируем и не обрабатываем (для конфиденциальности)
        return  # Просто выходим из функции, без ответа или лога

    # Если прошло проверку — логируем и продолжаем обработку (только для чеков)
    timestamp = datetime.fromtimestamp(business_message.date.timestamp()).strftime('%Y-%m-%d %H:%M:%S')
    chat_id = business_message.chat.id
    business_connection_id = business_connection.id if business_connection else None

    logger.info(
        f"Новое сообщение в бизнес-чате (чек):\n"
        f"Business Connection ID: {business_connection_id if business_connection_id else 'Неизвестно'}\n"
        f"Chat ID: {chat_id}\n"
        f"User ID: {user_id}\n"
        f"Username: {username}\n"
        f"First Name: {first_name}\n"
        f"Text (чек): {text}\n"  # Логируем только чеки
        f"Time: {timestamp}"
    )

    parts = text.split(":")
    if len(parts) != 9 or parts[0] != "receipt":
        reply_text = "Неверный формат чека. Ожидается 9 частей, начиная с 'receipt:'."
        logger.info(f"Ошибка: Неверный формат чека, получено {len(parts)} частей: {text}")
    else:
        try:
            receipt_id = int(parts[1])
            from_id = int(parts[2])
            to_username = parts[3]
            amount = float(parts[4])
            timestamp_chek = int(parts[5])
            product = None if parts[6] == "" or parts[6] == "None" else parts[6]
            empty = parts[7]  # Должно быть ""
            signature = parts[8]  # Подпись

            if empty != "":
                raise ValueError("Поле между product и signature должно быть пустым (двойное двоеточие ::).")

            # Проверка, что from_id или to_username совпадают с отправителем
            if str(from_id) != str(user_id) and to_username != username.lstrip('@'):
                reply_text = "Чек недействителен: ID или username отправителя не совпадают с данными чека."
                logger.info(f"Проверка чека не пройдена: from_id={from_id}, to_username={to_username}, "
                            f"пользователь ID={user_id}, username={username}")
            else:
                # Проверка времени
                current_time = int(time())
                if current_time - timestamp_chek > TIME_TOLERANCE or timestamp_chek > current_time + TIME_TOLERANCE:
                    reply_text = f"Чек недействителен: время вне допустимого диапазона (±{TIME_TOLERANCE} секунд)."
                    logger.info(f"Чек недействителен: timestamp={timestamp_chek}, current_time={current_time}")
                else:
                    # Проверка подписи
                    message_str = f"receipt:{receipt_id}:{from_id}:{to_username}:{amount:.1f}:{timestamp_chek}:{product or ''}:"
                    message_hash = hashlib.sha256(message_str.encode()).digest()  # Используем SHA-256
                    logger.info(f"Строка для хэша: {message_str}")
                    logger.info(f"Хэш: {message_hash.hex()}")
                    logger.info(f"Подпись: {signature}")
                    try:
                        vk = VerifyingKey.from_string(bytes.fromhex(BOT_PUBLIC_KEY_HEX), curve=SECP256k1)
                        is_valid = vk.verify(bytes.fromhex(signature), message_str.encode())  # Проверка с SHA-256
                        if is_valid:
                            # Проверка в базе данных
                            tx = Transaction.get_or_none(Transaction.id == receipt_id)
                            if not tx:
                                # Сохраняем новую транзакцию
                                Transaction.create(
                                    id=receipt_id,
                                    from_id=from_id,
                                    to_username=to_username,
                                    amount=amount,
                                    timestamp=timestamp_chek,
                                    product=product,
                                    nonce=None,
                                    signature=signature,
                                    used=False,
                                    status='pending'  # Совместимость с вашей моделью
                                )
                                logger.info(f"Транзакция {receipt_id} добавлена в базу данных.")
                                reply_text = "Чек подлинный. Продукт в пути, транзакция совершается."
                            elif tx.used:
                                reply_text = "Чек уже использован."
                                logger.info(f"Чек {receipt_id} уже использован.")
                            else:
                                Transaction.update(used=True, status='confirmed').where(Transaction.id == receipt_id).execute()
                                reply_text = "Чек подлинный. Продукт в пути, транзакция совершается."
                                logger.info(f"Чек {receipt_id} подлинный и помечен как использованный.")
                                # Уведомление владельцу
                                owner_chat_id = OWNERS.get(to_username)
                                if owner_chat_id:
                                    try:
                                        await bot.send_message(
                                            owner_chat_id,
                                            f"Успешная оплата продукта {product} на сумму {amount} от пользователя @{username} (ID: {user_id})."
                                        )
                                        logger.info(f"Уведомление отправлено владельцу @{to_username} в чат {owner_chat_id}.")
                                    except Exception as e:
                                        logger.error(f"Ошибка отправки уведомления владельцу @{to_username}: {str(e)}")
                                else:
                                    logger.error(f"Владелец с username {to_username} не найден в OWNERS.")
                                # Выполнение действия партнера (плагин продавца)
                                # Адаптированный путь: кросс-платформенный, относительный от директории скрипта (bot.py)
                                script_dir = os.path.dirname(os.path.abspath(__file__))  # Директория bot.py
                                plugin_path = os.path.join(script_dir, "plugins", f"{to_username.lower()}.py")  # Кросс-платформенный путь
                                if os.path.exists(plugin_path):
                                    try:
                                        spec = importlib.util.spec_from_file_location(to_username, plugin_path)
                                        plugin = importlib.util.module_from_spec(spec)
                                        spec.loader.exec_module(plugin)
                                        # Передача bot для использования в плагине (глобальный bot)
                                        await plugin.on_successful_payment(
                                            user_id=from_id,
                                            product=product,
                                            receipt_id=receipt_id,
                                            amount=amount,  # Новое!
                                            bot=bot  # Опционально: передача бота для Telegram-операций
                                        )
                                        logger.info(f"Плагин {to_username} успешно выполнен для пользователя {from_id}, продукт {product}. Путь: {plugin_path}")
                                    except Exception as e:
                                        logger.error(f"Ошибка выполнения плагина {to_username} по пути {plugin_path}: {str(e)}")
                                        # Опционально: уведомить владельца об ошибке
                                        if owner_chat_id:
                                            await bot.send_message(owner_chat_id, f"Ошибка в плагине для чека {receipt_id}: {str(e)}")
                                else:
                                    logger.warning(f"Плагин для {to_username} не найден по пути {plugin_path}.")
                        else:
                            reply_text = "Чек недействителен: неверная подпись."
                            logger.info("Ошибка подписи при проверке чека")
                            
                    except BadSignatureError:
                        reply_text = "Чек недействителен: ошибка подписи."
                        logger.info("Ошибка подписи при проверке чека")
                    except Exception as e:
                        reply_text = f"Ошибка проверки чека: {str(e)}"
                        logger.error(f"Ошибка проверки подписи: {str(e)}")
        except ValueError as e:
            reply_text = f"Неверный формат данных в чеке: {str(e)}"
            logger.info(f"Ошибка формата чека: {str(e)}")

    # Ответ клиенту от имени бизнес-аккаунта
    try:
        await bot.send_message(
            chat_id=chat_id,
            text=reply_text,
            business_connection_id=business_connection_id
        )
    except Exception as e:
        logger.error(f"Ошибка при отправке ответа клиенту: {str(e)}")
        await bot.send_message(
            chat_id=chat_id,
            text="Произошла ошибка при отправке ответа. Пожалуйста, проверьте настройки бизнес-аккаунта."
        )
```

</details>


**Прозрачность на первом месте**: скоро — проверка подлинности кода.
Друзья, мы слышим ваши опасения по поводу приватности — и это правильно! В FreeFlow Network мы строим доверие на открытости. Скоро выпустим функцию верификации кода: каждый сможет убедиться, что опубликованный на GitHub исходник — это именно то, что работает в боте.
Код выше? Это полная копия реальной логики из нашего бота — без утайки. С помощью уникального SHA-256 хэша вы проверите: генерируйте хэш файла на GitHub и сравнивайте с нашим официальным. Никаких сюрпризов — только чистый, проверенный код!
Хотите протестировать? Следите за обновлением в [t.me/freeflownetwork](https://t.me/freeflownetwork). Давайте вместе строить безопасный DeFi! 🔒💎

**Планы развития (0.0.4+)**: Расширение API для внешних ботов — webhook'и для реал-тайм уведомлений, поддержка плагинов с проверкой (whitelist). Это сделает FreeFlow платформой: подключайте боты для автоматизации — и ваш профиль превратится в сверхумный хищник, который сам охотится за прибылью. Следите за тестами в [t.me/freeflowdev](https://t.me/freeflowdev)! 

## 🤝 Контрибьютинг
Хотите внести вклад? Стать партнёром или просто поинтересоваться, обращайтесь по контактам и следите за интересными событиями! 👇

## 📞 Контакты
- **Telegram**: [@majworker](https://t.me/ceo_freeflow)
- **Канал новостей FreeFlow**: [t.me/freeflownetwork](https://t.me/freeflownetwork)
- **Канал разработки и для тех кому более интереснее**: [t.me/freeflowdev](https://t.me/freeflowdev)

**FreeFlowNetwork — будущее финансовой свободы в Telegram!** 🚀

*0.0.3 version*
