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

# Auto-generated tests (2025-05-20T18:49:59.831783)
def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3
    assert calc.add(-1, 1) == 0

def test_subtract():
    calc = Calculator()
    assert calc.subtract(5, 2) == 3
    assert calc.subtract(2, 5) == -3

def test_multiply():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(0, 5) == 0

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5
    assert calc.divide(10, -2) == -5

    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_get_last_result():
    calc = Calculator()
    assert calc.get_last_result() == 0
    calc.add(5, 2)
    assert calc.get_last_result() == 7

def test_clear_last_result():
    calc = Calculator()
    calc.add(1, 1)
    calc.clear_last_result()
    assert calc.get_last_result() == 0