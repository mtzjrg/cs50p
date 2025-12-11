# Seasons of Love: Implement one or more functions that test your implementation
#       of any functions besides `main` in `seasons.py` thoroughly, each of
#       whose names should begin with `test_` so that you can execute your tests
#       with `pytest test_seasons.py`

import pytest

from seasons import convert


def test_str():
    with pytest.raises(ValueError):
        convert("February 6th, 1998")

def test_iso():
    with pytest.raises(ValueError):
        convert("02-06-1998")
