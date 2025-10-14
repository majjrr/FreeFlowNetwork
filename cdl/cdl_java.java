import java.text.DecimalFormat;
import java.util.logging.Logger;

public class DeepLinkUtils {
    private static final Logger logger = Logger.getLogger(DeepLinkUtils.class.getName());
    private static final DecimalFormat df = new DecimalFormat("#.##");

    public static String createDeepLink(String botUsername, String recipient, double amount, String product) {
        // Убрать @
        recipient = recipient.replaceAll("^@", "");

        // Валидация
        if (amount <= 0 || recipient.length() > 32 || product.length() > 20 || product.contains(" ")) {
            logger.severe("Неверные параметры для deep link");
            return null;
        }
        // Заглушка для мата (реализуйте filterProfanity)
        if (!filterProfanity(recipient) || !filterProfanity(product)) {
            logger.severe("Недопустимые слова в параметрах");
            return null;
        }

        // Форматирование amount
        String amountStr = df.format(amount).replace(".", "_");

        // Параметр start
        String payParam = String.format("pay_to_%s_%s_%s", recipient, amountStr, product);
        if (payParam.length() > 64) {
            logger.severe(String.format("Параметр слишком длинный: %d > 64", payParam.length()));
            return null;
        }

        // Ссылка
        String deepLink = String.format("https://t.me/%s?start=%s", botUsername, payParam);
        logger.info("Создана deep link: " + deepLink);
        return deepLink;
    }

    private static boolean filterProfanity(String str) {
        // Реализуйте: return !str.matches(".*(badword).*");
        return true; // Заглушка
    }

    // Пример
    public static void main(String[] args) {
        String link = createDeepLink("FreeFlowNetwork_bot", "majworker", 0.10, "9999A");
        System.out.println(link); // https://t.me/FreeFlowNetwork_bot?start=pay_to_majworker_0_10_9999A
    }
}