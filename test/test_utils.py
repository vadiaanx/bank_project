from src.utils import amount_in_rub


def test_amount_in_rub_rub_ok():
    tx = {"operationAmount": {"amount": "31957.58", "currency": {"code": "RUB"}}}
    assert amount_in_rub(tx) == 31957.58
