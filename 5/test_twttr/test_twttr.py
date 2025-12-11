# Testing my twttr: Implement one or more functions that collectively test
#       your implementations of `shorten` thoroughly, each of whose names
#       should begin with `test_` so that you can execute your tests with:
#       `pytest test_twttr.py`

from twttr import shorten

def test_lower():
    assert shorten("dog") == "dg"

def test_upper():
    assert shorten("DOG") == "DG"

def test_nums():
    assert shorten("CS50") == "CS50"

def test_punc():
    assert shorten("What's your name?") == "Wht's yr nm?"
