import pytest
from src.calculator import Calculator

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

# Note: We're intentionally leaving some functions untested
# to demonstrate the coverage workflow

# Auto-generated tests
Here are some comprehensive unit tests using pytest for the Calculator class. These tests aim to achieve high coverage of the Calculator's methods:

```python
import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_initial_result(calculator):
    assert calculator.get_last_result() == 0

def test_addition(calculator):
    assert calculator.add(2, 3) == 5
    assert calculator.get_last_result() == 5

def test_subtraction(calculator):
    assert calculator.subtract(5, 3) == 2
    assert calculator.get_last_result() == 2

def test_multiplication(calculator):
    assert calculator.multiply(2, 3) == 6
    assert calculator.get_last_result() == 6

def test_division(calculator):
    assert calculator.divide(10, 2) == 5
    assert calculator.get_last_result() == 5

def test_division_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(10, 0)

def test_clear_last_result(calculator):
    calculator.add(2, 3)
    calculator.clear_last_result()
    assert calculator.get_last_result() == 0

def test_chained_operations(calculator):
    calculator.add(5, 2)
    assert calculator.add(3, 4) == 7

def test_division_result(calculator):
    result = calculator.divide(10, 3)
    assert result == pytest.approx(3.3333, rel=1e-4)
```

These tests cover various scenarios for each method in the Calculator class, including basic arithmetic operations, handling division by zero, clearing the last result, and chaining multiple operations.

Make sure to adjust the import statement `from calculator import Calculator` based on the location of your Calculator class file. Run these tests using `pytest` to check the functionality of your Calculator class.