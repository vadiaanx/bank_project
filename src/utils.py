import json
import os

from external_api import get_rate_to_rub


def load_transactions(file_path):
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            if os.path.getsize(file_path) == 0:
                return []

            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except Exception:
        return []


def amount_in_rub(transaction: dict[str, any]) -> float:
    """
    Принимает транзакцию в формате вашего JSON и возвращает сумму в рублях (float).
    - Если currency.code == USD/EUR — конвертируем по текущему курсу.
    - Если RUB или поле отсутствует/битое — возвращаем то, что можно безопасно преобразовать (или 0.0).
    """
    if not isinstance(transaction, dict):
        return 0.0

    op = transaction.get("operationAmount") or {}
    amount_str = (op.get("amount") or "").strip()
    currency = ((op.get("currency") or {}).get("code") or "RUB").upper()

    # Пытаемся превратить строку в число
    try:
        amount = float(amount_str.replace(",", "."))  # на всякий случай, если запятая
    except (TypeError, ValueError):
        return 0.0

    # Конвертация только для USD/EUR по условию задачи
    if currency in ("USD", "EUR"):
        try:
            rate = get_rate_to_rub(currency)
            return amount * rate
        except Exception:
            # В учебных целях не роняем код — если курс не получили, вернём 0.0
            return 0.0

    # Всё остальное считаем рублями
    return amount
