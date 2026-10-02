import pytest
from twttr import shorten

def test_default():
    assert shorten() == "Twttr"

def test_argument():
    assert shorten("Witter") == "Wttr"