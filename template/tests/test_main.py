import pytest

from main import greet


def test_greet(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("GREETING", "Hi")
    assert greet("world") == "Hi, world!"
