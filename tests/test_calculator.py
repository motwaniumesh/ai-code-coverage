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

# Auto-generated tests (2025-05-21T15:15:30.817497)
def test_add():
    calc = Calculator()
    assert calc.add(3, 4) == 7
    assert calc.get_last_result() == 7

def test_subtract():
    calc = Calculator()
    assert calc.subtract(8, 5) == 3
    assert calc.get_last_result() == 3

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 5) == 10
    assert calc.get_last_result() == 10

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.get_last_result() == 5

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(8, 0)
    assert calc.get_last_result() == 0

def test_clear_last_result():
    calc = Calculator()
    calc.add(2, 3)
    assert calc.get_last_result() == 5
    calc.clear_last_result()
    assert calc.get_last_result() == 0