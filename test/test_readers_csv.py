from unittest.mock import MagicMock, patch

import pandas as pd

from src.readers_csv_excel import read_transactions_from_csv


@patch("src.readers_csv_excel.pd.read_csv")
def test_read_transactions_from_csv_returns_list_of_dicts(mock_read_csv):
    # Готовим фейковый DataFrame
    data = {
        "date": ["2025-01-01", "2025-01-02"],
        "amount": [100, -50],
        "category": ["Salary", "Groceries"],
    }
    fake_df = pd.DataFrame(data)

    # Настраиваем mock: когда в коде вызовется pd.read_csv,
    # он вернёт наш fake_df
    mock_read_csv.return_value = fake_df

    # Вызываем функцию
    result = read_transactions_from_csv("transactions.csv")

    # Проверяем, что read_csv вообще вызывался с нужным аргументом
    mock_read_csv.assert_called_once_with("transactions.csv", sep=";")

    # Проверяем формат результата
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["date"] == "2025-01-01"
    assert result[0]["amount"] == 100
    assert result[0]["category"] == "Salary"