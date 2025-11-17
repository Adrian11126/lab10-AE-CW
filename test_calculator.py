#https://github.com/Adrian11126/lab10-AE-WC.git
# Partner roles: Adrian (Partner 1), Camryn (Partner 2)

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    # Partner section (example — yours may differ)
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(10, 3), 7)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(-2, -4), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)   # dividing by zero because a == 0

    def test_logarithm(self):
        # log base 2 of 8 = 3
        self.assertEqual(logarithm(8, 2), 3)

    def test_log_invalid_base(self):
        # base cannot be 1 or negative
        with self.assertRaises(ValueError):
            logarithm(10, 1)

        with self.assertRaises(ValueError):
            logarithm(10, -2)

    # Your partner's tests (you don't edit these)
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)  # b / a = 10 / 2
        self.assertEqual(div(5, -15), -3)

    def test_log_invalid_argument(self):
        # log of a negative number is invalid
        with self.assertRaises(ValueError):
            logarithm(-5, 2)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertAlmostEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 1.41421356237, places=5)


if __name__ == '__main__':
    unittest.main()
