# Back to the Bank: Implement three or more functions that collectively test
#       your implementations of `value` thoroughly, each of whose names should
#       being with `test_` so that you can execute your tests with:
#       `pytest test_bank.py`

from bank import value

def test_zero():
    assert value("Hello, sir.") == 0

def test_twenty():
    assert value("hey, what's up?") == 20

def test_hundred():
    assert value("  Do I know you? ") == 100
