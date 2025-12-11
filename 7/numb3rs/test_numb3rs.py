# NUMB3RS: Implement two or more functions that collectively test your
#       implementation of `validate` thoroughly, each of whose names should
#       begin with `test_` so that you can execute your tests with:
#       `pytest test_numbers.py`

from numb3rs import validate


def test_valid():
    assert validate("255.255.0.0")

def test_invalid():
    assert not validate("255.256.0.0")

def test_len():
    assert not validate("1.2.3")
    assert not validate("1.2.3.4.5")

def test_str():
    assert not validate("cat")
