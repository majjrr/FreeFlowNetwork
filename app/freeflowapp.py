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


import flet as ft
from ecdsa import VerifyingKey, SECP256k1, BadSignatureError
import time
import random

# Константы из бота
# BOT_PUBLIC_KEY_HEX - Может меняться с обновлениями, пожалуйста попросите его у @majworker или вставьте новый через команду /start
BOT_PUBLIC_KEY_HEX = "00e3614c68b0cdebdf654651a9fee7cbbe79e768f444792540a505e64dc8df3c981428aba7bf6b5984eea9fe061eb082bfabb56c5b54b77c749c9a0e5d903587"
TIME_TOLERANCE = 300  # 5 минут в секундах
EXPECTED_AMOUNT = 10.0  # Фиксированная сумма для проверки (в $FFT)
VERSION = "0.0.1"

def main(page: ft.Page):
    page.title = "FreeFlowNetwork Check Verifier"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLACK
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Установка размеров окна и запрет изменения размера
    page.window.width = 400
    page.window.height = 700
    page.window.min_width = 400
    page.window.min_height = 700
    page.window.max_width = 400
    page.window.max_height = 700
    page.window.resizable = False

    # Поле для ввода чека
    receipt_input = ft.TextField(
        label="Вставьте чек",
        multiline=True,
        height=120,
        width=340,
        border_color=ft.Colors.BLUE_400,
        focused_border_color=ft.Colors.BLUE_800,
        hint_text="receipt:tx_id:from_id:to_username:amount:timestamp:product:operation:sig_hex",
        text_style=ft.TextStyle(color=ft.Colors.WHITE),
        bgcolor=ft.Colors.GREY_900,
        border_radius=8,
    )

    # Поле для отображения результата
    result_text = ft.Text(
        "",
        color=ft.Colors.WHITE,
        size=14,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    # Поле для случайного кода и суммы
    random_code_text = ft.Text(
        f"Сгенерируйте код для product (Сумма: {EXPECTED_AMOUNT} $FFT)",
        color=ft.Colors.GREY_400,
        size=12,
        italic=True,
        text_align=ft.TextAlign.CENTER,
    )

    # Кнопка для генерации случайного 6-значного кода
    def generate_random_code(e):
        random_code = random.randint(100000, 999999)  # 6-значный код
        random_code_text.value = f"Код: {random_code}, Сумма: {EXPECTED_AMOUNT} $FFT\n(Используйте код в 'product' при переводе)"
        random_code_text.color = ft.Colors.CYAN_300
        page.update()

    generate_code_button = ft.ElevatedButton(
        text="Сгенерировать код",
        on_click=generate_random_code,
        width=340,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN_700,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=15,
            elevation={"pressed": 2, "": 8},
            animation_duration=300,
        ),
        icon=ft.Icons.CODE,
    )

    # Функция проверки чека
    def verify_receipt(e):
        receipt = receipt_input.value.strip()

        # Проверка заполнения поля чека
        if not receipt:
            result_text.value = "Введите чек!"
            result_text.color = ft.Colors.RED
            page.update()
            return

        # Парсинг чека
        data_parts = receipt.split(":")
        if len(data_parts) != 9 or data_parts[0] != "receipt":
            result_text.value = "Неверный формат чека!"
            result_text.color = ft.Colors.RED
            page.update()
            return

        try:
            tx_id, from_id, to_username, amount, timestamp, product, operation, sig_hex = data_parts[1:]
            amount = float(amount)
            timestamp = int(timestamp)
            from_id = int(from_id)
            tx_id = int(tx_id)
            product = product if product else ''
            operation = operation if operation else ''
        except ValueError:
            result_text.value = "Ошибка в данных чека!"
            result_text.color = ft.Colors.RED
            page.update()
            return

        # Проверка суммы
        if abs(amount - EXPECTED_AMOUNT) > 0.001:  # Учитываем погрешность
            result_text.value = f"Сумма не совпадает! В чеке: {amount}, ожидалось: {EXPECTED_AMOUNT}"
            result_text.color = ft.Colors.RED
            page.update()
            return

        # Проверка времени
        if timestamp > time.time() + TIME_TOLERANCE:
            result_text.value = "Чек из будущего - недействителен!"
            result_text.color = ft.Colors.RED
            page.update()
            return

        # Проверка подписи
        message = f"receipt:{tx_id}:{from_id}:{to_username}:{amount}:{timestamp}:{product}:{operation}".encode()
        try:
            vk = VerifyingKey.from_string(bytes.fromhex(BOT_PUBLIC_KEY_HEX), curve=SECP256k1)
            if vk.verify(bytes.fromhex(sig_hex), message):
                result_text.value = (
                    f"Чек подлинный!\n"
                    f"Транзакция ID: {tx_id:06d}\n"  # Форматируем как 6-значный
                    f"От: {from_id}\n"
                    f"Для: @{to_username}\n"
                    f"Сумма: {amount:.2f} $FFT\n"
                    f"Время: {time.ctime(timestamp)}\n"
                    f"Product: {product or 'Нет'}\n"
                    f"Operation: {operation or 'Нет'}"
                )
                result_text.color = ft.Colors.GREEN
            else:
                result_text.value = "Неверная подпись!"
                result_text.color = ft.Colors.RED
        except BadSignatureError:
            result_text.value = "Ошибка подписи!"
            result_text.color = ft.Colors.RED
        except Exception as ex:
            result_text.value = f"Ошибка: {str(ex)}"
            result_text.color = ft.Colors.RED

        page.update()

    # Кнопка проверки
    verify_button = ft.ElevatedButton(
        text="Проверить чек",
        on_click=verify_receipt,
        width=340,
        icon=ft.Icons.CHECK_CIRCLE_OUTLINE,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_700,
            color=ft.Colors.WHITE,
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=15,
            elevation={"pressed": 2, "": 8},
            animation_duration=300,
        ),
    )

    # Заголовок
    header = ft.Text(
        "FreeFlowNetwork Verifier",
        size=24,
        color=ft.Colors.BLUE_300,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    # Карточка с анимацией
    card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    header,
                    ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                    generate_code_button,
                    random_code_text,
                    ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                    receipt_input,
                    verify_button,
                    ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                    ft.Container(
                        content=result_text,
                        padding=10,
                        border=ft.border.all(1, ft.Colors.GREY_700),
                        border_radius=10,
                        width=340,
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.GREY_900,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            padding=20,
        ),
        elevation=10,
        shape=ft.RoundedRectangleBorder(radius=15),
        color=ft.Colors.GREY_900,
        animate_opacity=True,
        animate_scale=True,
    )

    # Основной контейнер с градиентом
    page.add(
        ft.Container(
            content=card,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[ft.Colors.BLUE_900, ft.Colors.PURPLE_900],
            ),
            width=380,
            height=580,
            border_radius=15,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)