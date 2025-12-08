# Учебный проект по Python для фильтрации и сортировки банковских операций.

## 📦 Установка и запуск

1. Клонируйте репозиторий:
```
git clone https://github.com/vadiaanx/bank_project.git
```
2. Установите Poetry, если он ещё не установлен:
```
curl -sSL https://install.python-poetry.org | python3 -
```

3. Установите зависимости:
```
poetry install
```
4. Активируйте виртуальное окружение:
```
poetry shell
```
5. Запустите основной скрипт:
```
python src/main.py
```

## ✅ Проверка качества кода
### Для проверки качества кода используются:
* flake8
* mypy
* black
* isort

### Команды для запуска:
```
flake8 .
mypy .
black .
isort .
```

## 🧪 Тестирование
Для тестирования используется **pytest**. Тесты находятся в папке `tests/`.

### Запуск всех тестов
`pytest`
### Запуск тестов с подробным выводом
`pytest -v`
### Запуск конкретного файла или теста
`pytest tests/test_masks.py`
`pytest -k "test_get_mask_card_number_valid"`
### Проверка покрытия тестами
(при установленном плагине `pytest-cov`):
`pytest --cov=src --cov-report=term-missing`

## Новый модуль: `generators.py`

В модуле реализованы генераторы для работы с транзакциями и банковскими картами:

- **`filter_by_currency(transactions, currency_code)`**  
  Генератор, который отбирает транзакции только с указанным кодом валюты.

- **`transaction_descriptions(transactions)`**  
  Генератор, который возвращает описания всех транзакций.

- **`card_number_generator(start, stop)`**  
  Генератор, формирующий номера карт в формате `XXXX XXXX XXXX XXXX` для чисел в диапазоне от `start` до `stop` включительно.

### 🔧 Примеры использования

#### 1. Фильтрация транзакций по валюте
```python
from src.generators import filter_by_currency

transactions = [
    {
        "id": 1,
        "operationAmount": {"amount": "100", "currency": {"name": "USD", "code": "USD"}},
        "description": "Оплата по счету",
    },
    {
        "id": 2,
        "operationAmount": {"amount": "200", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод средств",
    },
]

usd_transactions = filter_by_currency(transactions, "USD")

for tx in usd_transactions:
    print(tx["id"], tx["description"])
# Вывод:
# 1 Оплата по счету
```
#### 2. Получение описаний транзакций
```python
from src.generators import transaction_descriptions

transactions = [
    {"description": "Перевод организации"},
    {"description": "Перевод с карты на карту"},
]

descriptions = transaction_descriptions(transactions)

print(next(descriptions))  # Перевод организации
print(next(descriptions))  # Перевод с карты на карту
```

#### 3. Генерация номеров карт
```python
from src.generators import card_number_generator

for card in card_number_generator(1, 3):
    print(card)

# Вывод:
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003
```
#### 4. Поддерживаемые форматы данных

Проект умеет считывать финансовые операции из разных источников:

- JSON-файл с транзакциями;
- CSV-файл (см. `transactions.csv`);
- Excel-файл в формате `.xlsx` (см. `transactions_excel.xlsx`).

Для чтения CSV и Excel используется библиотека `pandas`.

Примеры использования:

```python
from src.readers_csv_excel import (
    read_transactions_from_csv,
    read_transactions_from_excel,
)

transactions_csv = read_transactions_from_csv("data/transactions.csv")
transactions_xlsx = read_transactions_from_excel("data/transactions_excel.xlsx")
```

🧪 Тестирование

Для функций модуля написаны автоматические тесты (см. `test/test_generators.py`)

###  2025-09-10
#### Added
- Новый модуль `decorators`:
  - Декоратор `log` для логирования выполнения функций.
  - Поддержка логирования как в **консоль**, так и в **файл** через параметр `filename`.
  - Логирование ошибок с указанием типа исключения и входных аргументов.

- Юнит-тесты для проверки корректной работы декоратора:
  - Тестирование успешного вызова функций.
  - Тестирование ошибок (например, `ZeroDivisionError`).
  - Проверка работы как с консольным выводом, так и с записью в файл.
- Поддержка отчётов покрытия тестов (pytest + pytest-cov, HTML-репорт).
