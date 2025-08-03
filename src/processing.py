from datetime import datetime


def filter_by_state(data: list[dict[str, str]], state: str = "EXECUTED") -> list[dict[str, str]]:
    """Фильтрует список словарей по значению ключа 'state'"""
    result = []
    for item in data:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(date: list[dict[str, str]], reverse: bool = True) -> list[dict[str, str]]:
    """Функция возвращает новый список, отсортированный по дате"""
    return sorted(date, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
