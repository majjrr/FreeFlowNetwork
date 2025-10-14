using System;
using System.Globalization;
using System.Text.RegularExpressions;

public class DeepLinkUtils
{
    private static readonly CultureInfo Culture = CultureInfo.InvariantCulture;

    public static string CreateDeepLink(string botUsername, string recipient, double amount, string product)
    {
        // Убрать @
        if (recipient.StartsWith("@"))
        {
            recipient = recipient.Substring(1);
        }

        // Валидация
        if (amount <= 0 || recipient.Length > 32 || product.Length > 20 || product.Contains(" "))
        {
            Console.Error.WriteLine("Неверные параметры для deep link");
            return null;
        }
        // Заглушка для мата (реализуйте FilterProfanity)
        if (!FilterProfanity(recipient) || !FilterProfanity(product))
        {
            Console.Error.WriteLine("Недопустимые слова в параметрах");
            return null;
        }

        // Форматирование amount
        string amountStr = amount.ToString("F2", Culture).Replace(".", "_");

        // Параметр start
        string payParam = $"pay_to_{recipient}_{amountStr}_{product}";
        if (payParam.Length > 64)
        {
            Console.Error.WriteLine($"Параметр слишком длинный: {payParam.Length} > 64");
            return null;
        }

        // Ссылка
        string deepLink = $"https://t.me/{botUsername}?start={payParam}";
        Console.WriteLine($"Создана deep link: {deepLink}");
        return deepLink;
    }

    private static bool FilterProfanity(string str)
    {
        // Реализуйте: return !Regex.IsMatch(str, "badword");
        return true;  // Заглушка
    }

    // Пример
    public static void Main()
    {
        string link = CreateDeepLink("FreeFlowNetwork_bot", "majworker", 0.10, "9999A");
        Console.WriteLine(link);  // https://t.me/FreeFlowNetwork_bot?start=pay_to_majworker_0_10_9999A
    }
}