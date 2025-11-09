import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_sum(self):
        c = Calculator(10, 5)
        self.assertEqual(c.sum(), 15)

    def test_subtract(self):
        c = Calculator(10, 5)
        self.assertEqual(c.subtract(), 5)

    def test_multiply(self):
        c = Calculator(4, 3)
        self.assertEqual(c.multiply(), 12)

    def test_divide(self):
        c = Calculator(10, 2)
        self.assertEqual(c.divide(), 5)

    def test_divide_by_zero(self):
        c = Calculator(10, 0)
        self.assertEqual(c.divide(), "Błąd: dzielenie przez 0!")

if __name__ == "__main__":
    unittest.main()