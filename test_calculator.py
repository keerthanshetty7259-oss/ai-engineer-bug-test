import pytest
from calculator import divide_numbers, calculate_average


def test_divide_numbers_normal():
    assert divide_numbers(10, 2) == 5.0
    assert divide_numbers(-3, 3) == -1.0


def test_divide_numbers_zero_divisor():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(5, 0)


def test_calculate_average_empty():
    assert calculate_average([]) == 0.0


def test_calculate_average_single():
    assert calculate_average([42]) == 42.0


def test_calculate_average_multiple():
    assert calculate_average([1, 2, 3, 4]) == 2.5
    assert calculate_average([10, 20, 30]) == 20.0
