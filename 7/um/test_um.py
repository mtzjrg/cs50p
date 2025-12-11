# Regular, um, Expressions: Implement three or more functions that collectively
#       test your implementation of `count` thoroughly, each of whose names
#       should begin with `test_` so that you can execute your tests with:
#       `pytest test_um.py`

from um import count


def test_success():
    assert count("um") == 1
    assert count("yummy") == 0

def test_punc():
    assert count("Um...") == 1

def test_word():
    assert count("Um, thanks for the album.") == 1
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums") == 2
