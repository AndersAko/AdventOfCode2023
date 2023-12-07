from day7 import rank

def test_rank():
    cards = "22332"
    actual = rank(cards)
    assert actual == "33223"

def test_