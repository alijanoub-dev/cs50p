from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello, friend") == 0

def test_h():
    assert value("hi") == 20
    assert value("HI") == 20
    assert value("Hey there") == 20

def test_no_h():
    assert value("welcome") == 100
    assert value("GOOD MORNING") == 100