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

# Auto-generated tests (2025-05-20T18:43:42.409852)
def test_calculator_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_calculator_subtract():
    calc = Calculator()
    assert calc.subtract(5, 3) == 2

def test_calculator_multiply():
    calc = Calculator()
    assert calc.multiply(2, 3) == 6

def test_calculator_divide():
    calc = Calculator()
    assert calc.divide(6, 3) == 2
    with pytest.raises(ValueError):
        calc.divide(6, 0)

def test_calculator_get_last_result():
    calc = Calculator()
    calc.add(2, 3)
    assert calc.get_last_result() == 5

def test_calculator_clear_last_result():
    calc = Calculator()
    calc.add(2, 3)
    calc.clear_last_result()
    assert calc.get_last_result() == 0