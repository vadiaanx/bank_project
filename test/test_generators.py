from collections.abc import Iterator
from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions() -> list[dict[str, Any]]:
    """Смешанные транзакции с разными валютами и разными структурами."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_by_currency_returns_only_requested_currency(sample_transactions: list) -> None:
    """Фильтрация возвращает только транзакции нужной валюты и ничего лишнего."""
    gen = filter_by_currency(sample_transactions, "USD")
    result = list(gen)
    assert result != []


def test_when_no_transactions_in_currency_returns_empty(sample_transactions: list) -> None:
    """Если транзакций в заданной валюте нет (например, EUR), должен вернуться пустой результат без ошибок."""
    gen = filter_by_currency(sample_transactions, "EUR")
    assert list(gen) == []


def test_empty_input_list_no_error() -> None:
    """Пустой список обрабатывается без ошибок — генератор просто пустой."""
    gen = filter_by_currency([], "USD")
    assert isinstance(gen, Iterator)
    assert list(gen) == []


def test_transaction_descriptions_names(sample_transactions: list[dict[str, Any]]) -> None:
    """Функция возвращает корректные описания для каждой транзакции."""
    gen = transaction_descriptions([])
    assert list(gen) == []


def test_transaction_descriptions_names2(sample_transactions: list[dict[str, Any]]) -> None:
    """Тестируйте работу функции с различным количеством входных транзакций, включая пустой список."""
    gen = transaction_descriptions([])
    result = list(gen)
    assert result == []


def test_returns_iterator() -> None:
    gen = card_number_generator(1, 1)
    assert isinstance(gen, Iterator)


def test_basic_range_1_to_5_values() -> None:
    gen = card_number_generator(1, 5)
    result = list(gen)
    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]


def test_start_greater_than_stop_yields_empty() -> None:
    assert list(card_number_generator(5, 1)) == []
