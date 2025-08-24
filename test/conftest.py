import pytest


@pytest.fixture
def sample_data_mixed():
    """Список со смешанными статусами и датами; часть элементов без 'state'."""
    return [
        {"id": "1", "state": "EXECUTED", "date": "2024-12-31"},
        {"id": "2", "state": "CANCELED", "date": "2025-01-01"},
        {"id": "4", "state": "PENDING", "date": "2025-01-03"},
    ]
