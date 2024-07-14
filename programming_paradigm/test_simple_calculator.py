import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1,-1), -2)
        self.assertEqual(self.calc.add(0,0), 0)
        self.assertEqual(self.calc.add(1.5,2.5), 4)
        # Add more assertions to thoroughly test the add method.
    def test_subtraction(self):
        """Test the subtraction method"""
        self.assertEqual(self.calc.subtract(4,2), 2)
        self.assertEqual(self.calc.subtract(-4,2), -6)
        self.assertEqual(self.calc.subtract(4,-2), 6)
        self.assertEqual(self.calc.subtract(-4,-2), -2)
        self.assertEqual(self.calc.subtract(3.5,2.5), 1)

    def test_multiplication(self):
        """test the multiplication method"""
        self.assertEqual(self.calc.multiply(2,3), 6)
        self.assertEqual(self.calc.multiply(-2,3), -6)
        self.assertEqual(self.calc.multiply(-2,-3), 6)
        self.assertEqual(self.calc.multiply(2,0), 0)
        self.assertEqual(self.calc.multiply(2.5,3.5), 8.75)

    def test_division(self):
        """test the division method"""
        self.assertEqual(self.calc.divide(6,2), 3)
        self.assertEqual(self.calc.divide(-6,2), -3)
        self.assertEqual(self.calc.divide(-6,-2), 3)
        self.assertEqual(self.calc.divide(0,2), 0)
        self.assertEqual(self.calc.divide(6.5,2.5), 2.6)

        # Testing division by zero
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

# Remember to write additional test methods for subtract, multiply, and divide.