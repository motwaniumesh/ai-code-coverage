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

# Auto-generated tests (2025-05-20T16:49:29.798441)
def test_calculator_initialization():
    calc = Calculator()
    assert calc.get_last_result() == 0

def test_addition():
    calc = Calculator()
    assert calc.add(3, 4) == 7

def test_subtraction():
    calc = Calculator()
    assert calc.subtract(8, 2) == 6

def test_multiplication():
    calc = Calculator()
    assert calc.multiply(5, 6) == 30

def test_division():
    calc = Calculator()
    assert calc.divide(10, 5) == 2

def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_get_last_result():
    calc = Calculator()
    calc.add(2, 3)
    assert calc.get_last_result() == 5

def test_clear_last_result():
    calc = Calculator()
    calc.add(2, 3)
    assert calc.get_last_result() == 5
    calc.clear_last_result()
    assert calc.get_last_result() == 0