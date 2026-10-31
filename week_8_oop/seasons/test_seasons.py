import pytest
from seasons import User

def test_valid_input():
    with pytest.raises(SystemExit):
        User("Invalid")

    with pytest.raises(SystemExit):
        User("2000-02-30")


def test_valid_result():
    user = User("2000-01-01")
    result = user.minutes_since_birth()
    assert isinstance(result, str)
    assert "minutes" not in result