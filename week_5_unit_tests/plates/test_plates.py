from plates import is_valid

def test_length():
    assert is_valid("AA") == True
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False

def test_first_char():
    assert is_valid("5AAA") == False
    assert is_valid("A5AA") == False  

def test_char_order():
    assert is_valid("AAA") == True
    assert is_valid("A2AA") == False
    assert is_valid("AAA44") == True
    assert is_valid("AAA4A") == False

def test_first_num():
    assert is_valid("AA404") == True
    assert is_valid("AA044") == False

def test_special_char():
    assert is_valid("AA 45") == False
    assert is_valid("AA.55") == False
    assert is_valid("AA50!") == False