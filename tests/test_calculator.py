import pytest
from src.calculator import Calculator

# Initial tests
def test_add():
    """Test addition functionality."""
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.get_last_result() == 0

def test_multiply():
    """Test multiplication functionality."""
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0, 5) == 0


def test_clear_last_result():
    """Test clearing last result."""
    calc = Calculator()
    calc.add(5, 5)
    assert calc.get_last_result() == 10
    calc.clear_last_result()
    assert calc.get_last_result() == 0

def test_last_result_tracking():
    """Test that last_result is properly tracked across operations."""
    calc = Calculator()
    calc.add(2, 2)
    assert calc.get_last_result() == 4
    calc.multiply(3, 3)
    assert calc.get_last_result() == 9

# Auto-generated tests (2025-05-20T16:57:49.310111)
def test_initial_result():
    calc = Calculator()
    assert calc.get_last_result() == 0

def test_addition():
    calc = Calculator()
    result = calc.add(3, 4)
    assert result == 7
    assert calc.get_last_result() == 7

def test_subtraction():
    calc = Calculator()
    result = calc.subtract(10, 5)
    assert result == 5
    assert calc.get_last_result() == 5

def test_multiplication():
    calc = Calculator()
    result = calc.multiply(2, 3)
    assert result == 6
    assert calc.get_last_result() == 6

def test_division():
    calc = Calculator()
    result = calc.divide(10, 2)
    assert result == 5
    assert calc.get_last_result() == 5

def test_division_by_zero():
    calc = Calculator()
    try:
        calc.divide(5, 0)
    except ValueError as e:
        assert str(e) == "Division by zero is not allowed"
    else:
        assert False

def test_clear_last_result():
    calc = Calculator()
    calc.add(4, 3)
    calc.clear_last_result()
    assert calc.get_last_result() == 0