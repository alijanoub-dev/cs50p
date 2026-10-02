from fuel import gauge
from fuel import convert
import pytest

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(65) == "65%"

def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("0/4") == 0

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("4/2")

    with pytest.raises(ValueError):
        convert("three/four")