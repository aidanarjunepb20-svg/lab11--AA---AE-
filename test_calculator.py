# test_calculator.py
import unittest
import math
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)

    def test_subtract_and_alias(self):
        self.assertEqual(calculator.subtract(5, 2), 3)
        self.assertEqual(calculator.sub(5, 2), 3)

    def test_multiply_and_alias(self):
        self.assertEqual(calculator.multiply(4, 5), 20)
        self.assertEqual(calculator.mul(3, -2), -6)

    def test_divide_behavior(self):
        # Per lab: divide(a, b) computes b / a
        self.assertAlmostEqual(calculator.divide(2, 10), 5.0)
        self.assertAlmostEqual(calculator.div(4, 12), 3.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 10)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 1)

    def test_logarithm_and_alias(self):
        self.assertAlmostEqual(calculator.logarithm(10, 1000), 3.0, places=7)
        self.assertAlmostEqual(calculator.log(2, 8), 3.0, places=7)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)
        with self.assertRaises(ValueError):
            calculator.log(0, 5)

    def test_log_invalid_value(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(10, 0)
        with self.assertRaises(ValueError):
            calculator.log(2, -1)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        # negative side input still yields correct hypotenuse
        self.assertAlmostEqual(calculator.hypotenuse(-3, 4), 5.0)

    def test_square_root(self):
        self.assertAlmostEqual(calculator.square_root(16), 4.0)
        with self.assertRaises(ValueError):
            calculator.square_root(-9)

    def test_exponent_and_alias(self):
        self.assertEqual(calculator.exponent(2, 5), 32)
        self.assertEqual(calculator.exp(3, 3), 27)

if __name__ == "__main__":
    unittest.main()
