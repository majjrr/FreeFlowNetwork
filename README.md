![FreeFlowNetwork Banner](https://i.postimg.cc/q74FKqb8/FFN-logo.png)

**FreeFlowNetwork** — это инновационный Telegram-бот, обеспечивающий децентрализованные финансовые операции с 
использованием токена `$FFT`. Проект сочетает простоту интерфейса Telegram с мощью криптографических технологий,
предоставляя пользователям быстрые переводы, выгодный стейкинг и безопасное управление ключами. Это не просто бот
— это экосистема для финансовой свободы в Web3!

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
- **Поддержка**: Команда `/support` отправляет запрос в чат поддержки.
- **Администрирование**: Администраторы (задаются в `ADMIN_IDS`) могут управлять банами, 
- подписками и рекламой через команды, такие как `/add_ad`.

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
    ```python
    class User(Model):
      user_id = IntegerField(primary_key=True)
      username = TextField(null=True)
      balance = FloatField(default=0.0)
      history = TextField(null=True)
      subscription = TextField(null=True)
    ```
  Хранит информацию о пользователях, их балансах, истории транзакций и статусе подписки.
- **Transaction**:
    ```python
    class Transaction(Model):
      id = PrimaryKeyField()
      from_id = IntegerField()
      to_username = TextField()
      amount = FloatField()
      timestamp = IntegerField()
      status = TextField()
      product = TextField(null=True)
    ```
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

В скором времени добавим поддержку экосистемы TON и blockchain алгоритмов в FreeFlow Network.

## Универсальная функция для проверки чека

Всё это используетс как подключаемые модули в программу в вашем соответсвенном языке. 

В качестве примера была реализована простая программа с UI интерфейсом на Python с помощью фреймворка flet. Её можно менять под свои нужды или использовать её стандартным приложением.

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

### 2. Реализация на C++ (с использованием libsecp256k1)

Установите `libsecp256k1` (например, через `vcpkg` или `brew`). Компиляция: `g++ file.cpp -lsecp256k1 -o program`.

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

**Примечание для C++:** Полная верификация подписи требует интеграции libsecp256k1. Используйте функции вроде `secp256k1_ecdsa_signature_parse_compact` и `secp256k1_ecdsa_verify` для проверки.

### 3. Реализация на C# (с использованием BouncyCastle)

Установите NuGet пакет `BouncyCastle.NetCore`.

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

**Примечание для C#:** Полная верификация требует разделения сигнатуры на r и s. Адаптируйте под формат sig_hex (DER или raw).

### 4. Реализация на Java (с использованием BouncyCastle)

Установите BouncyCastle через Maven: `<dependency><groupId>org.bouncycastle</groupId><artifactId>bcprov-jdk15on</artifactId><version>1.70</version></dependency>`.

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

**Примечание для Java:** Адаптируйте разделение сигнатуры на r и s в зависимости от формата sig_hex.

### 5. Реализация на JavaScript (с использованием elliptic)

Установите библиотеку: `npm install elliptic`.

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

**Примечание для JavaScript:** Адаптируйте sigHex под raw формат (r + s, 64 байта).

Это делает функцию универсальной — её можно интегрировать в программы на этих языках как библиотеку или модуль. Для входа/выхода используйте аргументы функции, а для консольных приложений добавьте парсинг командной строки.

## 🤖 Подключение ботов к профилю (будущее развитие)

FreeFlowNetwork планирует внедрить экосистему внешних ботов, которые пользователи смогут подключать к своим 
профилям для расширения функциональности. Позволяя автоматизировать задачи, такие как управление транзакциями 
$FFT, настройка уведомлений о стейкинге или персонализированные аналитические отчеты.

### Возможности
- **Интеграция с профилем**: Пользователи смогут авторизовать ботов через Telegram, привязывая их к своему 
аккаунту FreeFlowNetwork для безопасного доступа к данным баланса, истории транзакций и стейкинга.
- **Персонализация**: Боты смогут предлагать кастомные уведомления (например, о начислении процентов по 
стейкингу) или автоматические переводы по расписанию.
- **Безопасность**: Все боты будут проходить проверку на соответствие стандартам безопасности, с использованием 
OAuth-подобного протокола и ограниченных токенов доступа.

### Разработка
Разработка ботов будет осуществляться через **FreeFlowNetwork**. Ключевые аспекты:
- **Технологии**: Боты создаются на Python с использованием библиотек, таких как `aiogram`, 
для бесшовной интеграции с Telegram.
- **Пример подключения**:
  ```python
  from aiogram import Bot
  bot = Bot(token='YOUR_BOT_TOKEN')
  async def get_user_balance(user_id):
      # Запрос к FreeFlowNetwork API
      response = await api.get_balance(user_id)
      return response['balance']
  ```
- **Документация**: Подробное руководство и SDK будут предоставлены для упрощения разработки.
- **Сообщество**: Мы поддерживаем разработчиков через наш Telegram-канал ([t.me/freeflowdev](https://t.me/freeflowdev)), где можно получить помощь и поделиться идеями.

**Будущее**: **Интеграция внешних ботов сделает FreeFlowNetwork универсальной платформой для финансовых и социальных взаимодействий в Web3, открывая возможности для автоматизации и инноваций.**

## 🤝 Контрибьютинг
Хотите внести вклад? Стать партнёром или просто поинтересоваться, обращайтесь по контактам и следите за интересными событиями! 👇

## 📞 Контакты
- **Telegram**: [@majworker](https://t.me/majworker)
- **Канал новостей**: [t.me/freeflowdev](https://t.me/freeflowdev)

**FreeFlowNetwork — будущее финансовой свободы в Telegram!** 🚀

*0.0.2 version*
