from typing import Any

import pandas as pd


def read_transactions_from_csv(csv_path: str) -> list[dict[str, Any]]:
    """ Открывает файл csv, читает данные как таблицу, превращает таблицу в список словарей """

    df = pd.read_csv(csv_path)
    return df.to_dict(orient="records")


def read_transactions_from_excel(excel_path: str) -> list[dict[str, Any]]:
    """ Открывает файл Excel, читает данные как таблицу, превращает таблицу в список словарей """

    df = pd.read_excel(excel_path)
    return df.to_dict(orient="records")