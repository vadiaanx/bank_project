import pytest

from src.decorators import log


def test_log_console_success(capsys):
    @log()
    def add(x, y):
        return x + y

    result = add(2, 3)
    assert result == 5

    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_log_console_error(capsys):
    @log()
    def div(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    captured = capsys.readouterr()
    assert "div error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out
