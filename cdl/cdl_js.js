function createDeepLink(botUsername, recipient, amount, product) {
    // Валидация
    recipient = recipient.replace(/^@/, ''); // Убрать @
    if (amount <= 0 || recipient.length > 32 || product.length > 20 || product.includes(' ')) {
        console.error("Неверные параметры для deep link");
        return null;
    }
    // Проверка мата (реализуйте свою функцию, здесь заглушка)
    function filterProfanity(str) { return !/badword/.test(str); } // Замените на реальную
    if (!filterProfanity(recipient) || !filterProfanity(product)) {
        console.error("Недопустимые слова в параметрах");
        return null;
    }

    // Форматирование amount
    const amountStr = amount.toFixed(2).replace('.', '_');

    // Параметр start
    const payParam = `pay_to_${recipient}_${amountStr}_${product}`;
    if (payParam.length > 64) {
        console.error(`Параметр слишком длинный: ${payParam.length} > 64`);
        return null;
    }

    // Ссылка
    const deepLink = `https://t.me/${botUsername}?start=${payParam}`;
    console.info(`Создана deep link: ${deepLink}`);
    return deepLink;
}

// Пример
const link = createDeepLink("FreeFlowNetwork_bot", "majworker", 0.10, "9999A");
console.log(link); // https://t.me/FreeFlowNetwork_bot?start=pay_to_majworker_0_10_9999A