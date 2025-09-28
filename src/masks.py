import logging
from typing import Any

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

if not logger.handlers:
    fh = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
    fh.setLevel(logging.DEBUG)

    fmt = logging.Formatter(
        fmt="%(asctime)s %(name)s %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    fh.setFormatter(fmt)

    logger.addHandler(fh)


def get_mask_card_number(card_number: int | str) -> Any:
    """Функция принимает на вход номер карты и возвращает ее маску."""

    card_number_str = str(card_number)

    # Проверка длины номера карты
    if len(card_number_str) != 16 or not card_number_str.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр.")

    # Формируем маску
    masked_card = card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
    logger.info("Сформирована маска карты **** **** **** %s", card_number_str[-4:])
    return masked_card


def get_mask_account(account_number: int | str) -> Any:
    """Функция принимает на вход номер счета и возвращает его маску."""

    account_number_str = str(account_number)

    # Проверка длины номера счета
    if len(account_number_str) != 20 or not account_number_str.isdigit():
        logger.error(
            "Некорректный номер счета: длина=%s, isdigit=%s", len(account_number_str), account_number_str.isdigit()
        )
        raise ValueError("Номер счета должен состоять из 20 цифр.")

    # Формируем маску
    masked_account = "**" + account_number_str[-4:]
    logger.info("Сформирована маска счета **%s", account_number_str[-4:])
    return masked_account
