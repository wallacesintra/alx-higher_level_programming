import unittest
import calc

class Test_calc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 10), 20)
        self.assertEqual(calc.add(-1, 10), 9)
        self.assertEqual(calc.add(-1, -3), -4)
    def test_subtract(self):
        self.assertEqual(calc.substract(10, 7), 3)
        self.assertEqual(calc.substract(-1, 10), -11)
        self.assertEqual(calc.substract(-1, -3), 2)        
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 7), 70)
        self.assertEqual(calc.multiply(-1, 10), -10)
        self.assertEqual(calc.multiply(-1, -3), 3)
    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        self.assertRaises(ValueError, calc.divide, 10, 0)
        """or"""
        with self.assertRaises(ValueError):
            calc.divide(10,0)


if __name__ == '__main__':
    unittest.main()