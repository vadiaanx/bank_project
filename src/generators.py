from collections.abc import Iterator

transactions = [
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


def filter_by_currency(transactions: list, currency_code: str) -> Iterator[str]:
    """Принимает на вход список словарей, представляющих транзакции, возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""
    for tx in transactions:
        if tx["operationAmount"]["currency"]["code"] == currency_code:
            yield tx


usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions: list) -> Iterator[str]:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for ds in transactions:
        yield ds["description"]


descriptions = transaction_descriptions(transactions)
for _ in range(2):
    print(next(descriptions))


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    for num in range(start, stop + 1):
        num_str = str(num).zfill(16)
        formatted = " ".join(num_str[i:i+4] for i in range(0, 16, 4))
        yield formatted


for card_number in card_number_generator(1, 5):
    print(card_number)
