from unittest.mock import Mock, patch

import external_api


@patch("external_api.requests.get")
def test_get_rate_to_rub_usd_ok(mock_get, monkeypatch):
    monkeypatch.setenv("EXCHANGE_RATES_API_KEY", "fake")
    mock_resp = Mock()
    mock_resp.raise_for_status.return_value = None
    mock_resp.json.return_value = {"rates": {"RUB": 95.0}}
    mock_get.return_value = mock_resp

    rate = external_api.get_rate_to_rub("USD")
    assert rate == 95.0


def test_get_rate_to_rub_rub_shortcut():
    assert external_api.get_rate_to_rub("RUB") == 1.0
