# import pytest
# from src.calculator import add, multiply

# def test_add():
#     assert add(2, 3) == 5

# def test_multiply():
#     assert multiply(2, 3) == 6

# test_calculator.py
import unittest
from src.calculator import add, multiply

class TestMyModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    # def test_multiply(self):
    #     self.assertEqual(multiply(5, 2), 10)
    #     self.assertEqual(multiply(1, 1), 1)
    #     self.assertEqual(multiply(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
