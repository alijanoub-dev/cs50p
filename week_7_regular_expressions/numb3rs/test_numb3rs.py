from numb3rs import validate

def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_invalid_range():
    assert validate("256.1.1.1") == False
    assert validate("1.512.1.1") == False
    assert validate("1.1.1.300") == False

def test_invalid_format():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("cat.dog.bird.fish") == False