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

# Auto-generated tests (2025-05-21T14:25:19.996337)
import pytest
from src.calculator import Calculator

def test_add():
    calculator = Calculator()
    assert calculator.add(4, 3) == 7

def test_subtract():
    calculator = Calculator()
    assert calculator.subtract(4, 3) == 1

def test_multiply():
    calculator = Calculator()
    assert calculator.multiply(4, 3) == 12

def test_divide():
    calculator = Calculator()
    assert calculator.divide(6, 3) == 2

def test_divide_by_zero():
    calculator = Calculator()
    with pytest.raises(ValueError):
        calculator.divide(6, 0)

def test_get_last_result():
    calculator = Calculator()
    calculator.add(4, 3)
    assert calculator.get_last_result() == 7

def test_clear_last_result():
    calculator = Calculator()
    calculator.add(4, 3)
    calculator.clear_last_result()
    assert calculator.get_last_result() == 0