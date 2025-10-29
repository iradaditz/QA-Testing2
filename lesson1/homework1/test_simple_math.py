import unittest
from simple_math import SimpleMath

class TestSimpleMath(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleMath()

    def test_square_positive(self):
        self.assertEqual(self.calc.square(2), 4)

    def test_square_negative(self):
        self.assertEqual(self.calc.square(-3), 9)

    def test_square_zero(self):
        self.assertEqual(self.calc.square(0), 0)

    def test_cube_positive(self):
        self.assertEqual(self.calc.cube(3), 27)

    def test_cube_negative(self):
        self.assertEqual(self.calc.cube(-3), -27)

    def test_cube_zero(self):
        self.assertEqual(self.calc.cube(0), 0)

if __name__ == '__main__':
    unittest.main()