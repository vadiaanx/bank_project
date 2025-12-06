from unittest.mock import patch

import pandas as pd

from src.readers_csv_excel import read_transactions_from_excel


@patch("src.readers_csv_excel.pd.read_excel")
def test_read_transactions_from_excel_returns_list_of_dicts(mock_read_excel):
    data = {
        "date": ["2025-02-01"],
        "amount": [200],
        "category": ["Bonus"],
    }
    fake_df = pd.DataFrame(data)
    mock_read_excel.return_value = fake_df

    result = read_transactions_from_excel("transactions_excel.xlsx")

    mock_read_excel.assert_called_once_with("transactions_excel.xlsx")

    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0]["category"] == "Bonus"