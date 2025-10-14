function createDeepLink($botUsername, $recipient, $amount, $product) {
    // Валидация
    $recipient = ltrim($recipient, '@');
    if ($amount <= 0 || strlen($recipient) > 32 || strlen($product) > 20 || strpos($product, ' ') !== false) {
        error_log("Неверные параметры для deep link");
        return null;
    }
    // Проверка мата (реализуйте свою функцию, здесь заглушка)
    function filterProfanity($str) { return !preg_match('/badword/', $str); } // Замените
    if (!filterProfanity($recipient) || !filterProfanity($product)) {
        error_log("Недопустимые слова в параметрах");
        return null;
    }

    // Форматирование amount
    $amountStr = str_replace('.', '_', number_format($amount, 2, '.', ''));

    // Параметр start
    $payParam = "pay_to_{$recipient}_{$amountStr}_{$product}";
    if (strlen($payParam) > 64) {
        error_log("Параметр слишком длинный: " . strlen($payParam) . " > 64");
        return null;
    }

    // Ссылка
    $deepLink = "https://t.me/{$botUsername}?start={$payParam}";
    error_log("Создана deep link: {$deepLink}");
    return $deepLink;
}

// Пример
$link = createDeepLink("FreeFlowNetwork_bot", "majworker", 0.10, "9999A");
echo $link; // https://t.me/FreeFlowNetwork_bot?start=pay_to_majworker_0_10_9999A