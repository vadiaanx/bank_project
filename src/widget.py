from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_number: str) -> str:
    """Функция принимает тип и номер карты или счета и возвращать строку с замаскированным номером"""

    if card_or_account_number.startswith("Счет"):
        name, number = card_or_account_number.split(maxsplit=1)
        return f"{name} {get_mask_account(number)}"
    else:
        name2, number2 = card_or_account_number.rsplit(" ", 1)
        return f"{name2} {get_mask_card_number(number2)}"


def get_date(date: str) -> str:
    """Функция принимает строку в формате "2024-03-11T02:26:18.671407"
    и возвращает строку в формате "ДД.ММ.ГГГГ", например "11.03.2024".
    """
    dt = datetime.fromisoformat(date)
    return dt.strftime("%d.%m.%Y")
