from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(sample_data_mixed):
    assert filter_by_state(sample_data_mixed) == [{"id": "1", "state": "EXECUTED", "date": "2024-12-31"}]
    assert filter_by_state(sample_data_mixed, state="CANCELED") == [
        {"id": "2", "state": "CANCELED", "date": "2025-01-01"}
    ]
    assert filter_by_state(sample_data_mixed, state="PENDING") == [
        {"id": "4", "state": "PENDING", "date": "2025-01-03"}
    ]


def test_sort_by_date(sample_data_mixed):
    assert sort_by_date(sample_data_mixed, reverse=False) == [
        {"date": "2024-12-31", "id": "1", "state": "EXECUTED"},
        {"date": "2025-01-01", "id": "2", "state": "CANCELED"},
        {"date": "2025-01-03", "id": "4", "state": "PENDING"},
    ]
    assert sort_by_date(sample_data_mixed) == [
        {"date": "2025-01-03", "id": "4", "state": "PENDING"},
        {"date": "2025-01-01", "id": "2", "state": "CANCELED"},
        {"date": "2024-12-31", "id": "1", "state": "EXECUTED"},
    ]
