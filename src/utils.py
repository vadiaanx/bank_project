import json
import logging
import os
from json import JSONDecodeError

from requests import RequestException

from external_api import get_rate_to_rub

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    fmt = logging.Formatter(
        fmt="%(asctime)s %(name)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(fmt)

    logger.addHandler(file_handler)


def load_transactions(file_path):
    logger.debug("Загрузка транзакций из файла: %s", file_path)
    if not os.path.exists(file_path):
        logger.warning("Файл не найден: %s — возвращаю пустой список", file_path)
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            if os.path.getsize(file_path) == 0:
                logger.info("Файл пустой: %s — возвращаю пустой список", file_path)
                return []

            data = json.load(f)
            if isinstance(data, list):
                logger.info("Успешно загружено транзакций: %d", len(data))
                return data
            else:
                logger.error("Неверный формат данных (ожидался list) — возвращаю пустой список")
                return []
    except FileNotFoundError:
        logger.exception("FileNotFoundError при открытии файла: %s", file_path)
        return []
    except JSONDecodeError:
        logger.exception("JSONDecodeError: повреждённый JSON в файле: %s", file_path)
        return []


def amount_in_rub(transaction: dict) -> float:
    """
    Принимает транзакцию в формате вашего JSON и возвращает сумму в рублях (float).
    - Если currency.code == USD/EUR — конвертируем по текущему курсу.
    - Если RUB или поле отсутствует/битое — возвращаем то, что можно безопасно преобразовать (или 0.0).
    """
    if not isinstance(transaction, dict):
        logger.error("amount_in_rub: на вход пришёл не dict, а %s", type(transaction))
        return 0.0

    op = transaction.get("operationAmount") or {}
    amount_str = (op.get("amount") or "").strip()
    currency = ((op.get("currency") or {}).get("code") or "RUB").upper()

    # Пытаемся превратить строку в число
    try:
        amount = float(amount_str.replace(",", "."))  # на всякий случай, если запятая
    except (TypeError, ValueError):
        logger.error("amount_in_rub: невозможно преобразовать сумму '%s' → float", amount_str)
        return 0.0

    # Конвертация только для USD/EUR по условию задачи
    if currency in ("USD", "EUR"):
        try:
            rate = get_rate_to_rub(currency)
            result = float(amount * rate)
            logger.info("Конвертация %s %.2f по курсу %.4f → RUB %.2f", currency, amount, rate, result)
            return result
        except (RequestException, RuntimeError, ValueError):
            logger.exception("Не удалось получить курс для %s — возвращаю 0.0", currency)
            # В учебных целях не роняем код — если курс не получили, вернём 0.0
            return 0.0

    logger.debug("Сумма в RUB без конвертации: %.2f", amount)  # Всё остальное считаем рублями
    return float(amount)
