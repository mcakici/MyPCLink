import unittest
from calculator import Calculator


class TestCalculatorAddition(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition_pos(self):
        self.assertEqual(9 + 2, self.calc.add(9, 2))

    def test_addition_neg(self):
        self.assertEqual(-9 + -2, self.calc.add(-9, -2))


class TestCalculatorSubtraction(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_subtraction(self):
        self.assertEqual(9-2, self.calc.sub(9, 2))


class TestCalculatorDivision(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_division(self):
        self.assertEqual(9/2, self.calc.div(9, 2))


class TestCalculatorMultiplication(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_multiplication(self):
        self.assertEqual(9*2, self.calc.mul(9, 2))


if __name__ == "__main__":
    unittest.main()
