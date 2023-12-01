import pytest

from Day1.day1 import convert, number2

def test_spelled_digits():
    input = "one, two, three, four, five, six, seven, eight, and nine"

    actual = number2(input)
    
    assert actual == 19

def test_shared_letter():
    input = "twoneight"
    expected = 28
    actual = int(number2(input))

    assert actual == expected

def test_shared_letter2():
    input = "twooneight"
    expected = 28
    actual = int(number2(input))

    assert actual == expected