from main import get_multiplicative_persistence
import pytest


def test_single_digit_returns_zero():
    assert get_multiplicative_persistence(0) == 0
    assert get_multiplicative_persistence(4) == 0
    assert get_multiplicative_persistence(9) == 0


def test_basic_examples():
    assert get_multiplicative_persistence(39) == 3
    assert get_multiplicative_persistence(999) == 4


def test_two_digit_numbers():
    assert get_multiplicative_persistence(25) == 2  # 2*5=10 → 1*0=0
    assert get_multiplicative_persistence(77) == 4  # chain


def test_numbers_with_zero():
    assert get_multiplicative_persistence(10) == 1
    assert get_multiplicative_persistence(101) == 1


def test_larger_numbers():
    assert get_multiplicative_persistence(444) == 3
    assert get_multiplicative_persistence(679) == 5


def test_one_step_cases():
    assert get_multiplicative_persistence(12) == 1
    assert get_multiplicative_persistence(20) == 1


def test_invalid_negative():
    with pytest.raises(ValueError):
        get_multiplicative_persistence(-39)
