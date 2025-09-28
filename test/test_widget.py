from typing import Any

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("Счет 00000000000000000000", "Счет **0000"),
        ("Счет 00123456000000007890", "Счет **7890"),
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Visa Classic 1234567812345678", "Visa Classic 1234 56** **** 5678"),
        ("MasterCard 0000000000000000", "MasterCard 0000 00** **** 0000"),
        ("My Super Card 9876543210987654", "My Super Card 9876 54** **** 7654"),
    ],
)
def test_mask_account_card_valid(raw: str, expected: str) -> None:
    assert mask_account_card(raw) == expected


@pytest.mark.parametrize("bad_value", ["1234567812345", "12345678123456789", "1234 5678 1234 5678"])
def test_get_mask_account_card_value_error(bad_value: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(bad_value)


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),  # только дата
        ("2024-02-29T00:00:00", "29.02.2024"),  # високосный год
        ("2024-03-11T02:26:18+00:00", "11.03.2024"),  # с таймзоной UTC
        ("2024-03-11T23:30:00+03:00", "11.03.2024"),  # с таймзоной +03:00
        ("2024-03-11T02:26:18Z", "11.03.2024"),
    ],
)  # 'Z' (UTC)
def test_get_date(raw: str, expected: str) -> None:
    assert get_date(raw) == expected


@pytest.mark.parametrize("bad", [None, 123, 12.34, [], {}])
def test_get_date_invalid_type(bad: Any) -> None:
    with pytest.raises(TypeError):
        get_date(bad)
