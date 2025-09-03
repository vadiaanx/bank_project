from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (1234567812345678, "1234 56** **** 5678"),
        ("1234567812345678", "1234 56** **** 5678"),
        ("0000000000000000", "0000 00** **** 0000"),
        ("0012345600007890", "0012 34** **** 7890"),
    ],
)
def test_get_mask_card_number_valid(card_number: int, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", [1234567898765432, "1234567898765332"])
def test_get_mask_card_number_groups(card_number: int) -> None:
    masked = get_mask_card_number(card_number)
    assert len(masked) == 19
    assert masked[4] == " "
    assert masked[7:9] == "**"
    assert masked[10:14] == "****"


@pytest.mark.parametrize(
    "bad_value",
    ["1234567812345", "12345678123456789", 123414124, "1234 5678 1234 5678", "12345678abcd5678", "", None, 0],
)
def test_get_mask_card_number_value_error(bad_value: Any) -> None:
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр."):
        get_mask_card_number(bad_value)


@pytest.mark.parametrize(
    "account_number, expected",
    [
        (12345678901234567890, "**7890"),
        ("12345678901234567890", "**7890"),
        ("00000000000000000000", "**0000"),
        ("00123456000000007890", "**7890"),
    ],
)
def test_get_mask_account_number_valid(account_number: int, expected: str) -> None:
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number", [12345678901234567890, "00123456000000007890"])
def test_get_mask_account_number_groups(account_number: int) -> None:
    masked = get_mask_account(account_number)
    assert len(masked) == 6
    assert masked[-6:-4] == "**"
    assert masked[2:].isdigit()


@pytest.mark.parametrize(
    "bad_value",
    [
        "1234567812345",
        "12345678123456789",
        123414124,
        "1234 5678 1234 5678",
        "12345678abcd5678",
        "",
        None,
        0,
        "-12345678901234567890",
    ],
)
def test_get_mask_account_number_value_error(bad_value: int) -> None:
    with pytest.raises(ValueError, match="Номер счета должен состоять из 20 цифр."):
        get_mask_account(bad_value)
