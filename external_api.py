import os

import requests
from dotenv import load_dotenv

load_dotenv()  # подтянет EXCHANGE_RATES_API_KEY из .env, если есть

api_url = "https://api.apilayer.com/exchangerates_data/latest"


def get_rate_to_rub(currency: str) -> float:
    """
    Возвращает курс: 1 <currency> = X RUB.
    Для RUB сразу вернёт 1.0.
    Бросает RuntimeError, если нет ключа или курс не найден.
    """
    currency = (currency or "RUB").upper()
    if currency == "RUB":
        return 1.0
    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    if not api_key:
        raise RuntimeError("EXCHANGE_RATES_API_KEY is not set in .env")

    headers = {"apikey": api_key}
    params = {"base": currency, "symbols": "RUB"}

    resp = requests.get(api_url, headers=headers, params=params, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    rate = data.get("rates", {}).get("RUB")
    if rate is None:
        raise RuntimeError(f"No RUB rate for base={currency}")
    return float(rate)
