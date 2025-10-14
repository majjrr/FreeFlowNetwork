def create_deep_link(bot_username: str, recipient: str, amount: float, product: str) -> str | None:
    """
    Универсальная функция для создания deep link.
    
    :param bot_username: Имя бота (например, 'FreeFlowNetwork_bot').
    :param recipient: Username получателя (без @, проверка на мат и длину).
    :param amount: Сумма (float > 0).
    :param product: Продукт (строка без пробелов, max 20 символов).
    :return: Готовая deep link или None при ошибке.
    """
    # Валидация (аналогично коду бота)
    recipient = recipient.lstrip('@')
    if amount <= 0 or len(recipient) > 32 or len(product) > 20 or ' ' in product:
        logger.error("Неверные параметры для deep link")
        return None
    if not filter_profanity(recipient) or not filter_profanity(product):  # Используйте вашу функцию
        logger.error("Недопустимые слова в параметрах")
        return None
    
    # Форматирование amount
    amount_str = f"{amount:.2f}".replace('.', '_')
    
    # Параметр start
    pay_param = f"pay_to_{recipient}_{amount_str}_{product}"
    if len(pay_param) > 64:
        logger.error(f"Параметр слишком длинный: {len(pay_param)} > 64")
        return None
    
    # Ссылка
    deep_link = f"https://t.me/{bot_username}?start={pay_param}"
    logger.info(f"Создана deep link: {deep_link}")
    return deep_link