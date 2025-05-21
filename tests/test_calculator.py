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

# Auto-generated tests (2025-05-21T14:11:34.871421)
# test_calculator.py

import pytest
from src.calculator import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(3, 4) == 7
    assert calc.get_last_result() == 7

def test_subtract():
    calc = Calculator()
    assert calc.subtract(10, 5) == 5
    assert calc.get_last_result() == 5

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6
    assert calc.get_last_result() == 6

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.get_last_result() == 5

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(5, 0)

def test_clear_last_result():
    calc = Calculator()
    calc.add(2, 3)
    calc.clear_last_result()
    assert calc.get_last_result() == 0