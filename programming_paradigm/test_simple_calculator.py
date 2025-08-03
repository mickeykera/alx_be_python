import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        # Basic addition tests
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        
        # Edge cases for addition
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)
        self.assertEqual(self.calc.add(-1000000, -2000000), -3000000)
        
        # Float addition tests
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
        self.assertEqual(self.calc.add(-1.5, 1.5), 0.0)
        
        # Type checking
        self.assertIsInstance(self.calc.add(1, 2), (int, float))
    
    def test_subtraction(self):
        # Basic subtraction tests
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        
        # Edge cases for subtraction
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(1000000, 500000), 500000)
        self.assertEqual(self.calc.subtract(-1000000, -500000), -500000)
        
        # Float subtraction tests
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)
        self.assertEqual(self.calc.subtract(1.5, 1.5), 0.0)
        
        # Type checking
        self.assertIsInstance(self.calc.subtract(1, 2), (int, float))
    
    def test_multiplication(self):
        # Basic multiplication tests
        self.assertEqual(self.calc.multiply(1, 2), 2)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        
        # Edge cases for multiplication
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)
        self.assertEqual(self.calc.multiply(-1000, 1000), -1000000)
        
        # Float multiplication tests
        self.assertEqual(self.calc.multiply(2.5, 2.0), 5.0)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.1), 0.01, places=7)
        self.assertEqual(self.calc.multiply(-2.5, 2.0), -5.0)
        
        # Type checking
        self.assertIsInstance(self.calc.multiply(1, 2), (int, float))
    
    def test_division(self):
        # Basic division tests
        self.assertEqual(self.calc.divide(1, 2), 0.5)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        self.assertEqual(self.calc.divide(-1, -1), 1)
        
        # Edge cases for division
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        
        # Division by zero tests
        self.assertIsNone(self.calc.divide(1, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-1, 0))
        self.assertIsNone(self.calc.divide(1000000, 0))
        
        # Float division tests
        self.assertEqual(self.calc.divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 1/3, places=7)
        self.assertEqual(self.calc.divide(-5.0, 2.0), -2.5)
        
        # Type checking for successful division
        result = self.calc.divide(1, 2)
        self.assertIsInstance(result, (int, float))
        
        # Type checking for division by zero
        result = self.calc.divide(1, 0)
        self.assertIsNone(result)
    
    def test_comprehensive_edge_cases(self):
        # Test with very large numbers
        self.assertEqual(self.calc.add(999999999, 1), 1000000000)
        self.assertEqual(self.calc.subtract(1000000000, 1), 999999999)
        self.assertEqual(self.calc.multiply(1000000, 1000000), 1000000000000)
        self.assertEqual(self.calc.divide(1000000, 2), 500000)
        
        # Test with very small numbers
        self.assertAlmostEqual(self.calc.add(0.000001, 0.000001), 0.000002, places=7)
        self.assertAlmostEqual(self.calc.multiply(0.000001, 0.000001), 0.000000000001, places=7)
        
        # Test with mixed types (int and float)
        self.assertEqual(self.calc.add(1, 1.5), 2.5)
        self.assertEqual(self.calc.multiply(2, 1.5), 3.0)
        self.assertEqual(self.calc.divide(3, 2), 1.5)
    
    def test_negative_numbers(self):
        # Comprehensive negative number tests
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        self.assertEqual(self.calc.divide(-6, -2), 3)
        
        # Mixed positive and negative
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.divide(-6, 2), -3)

if __name__ == "__main__":
    unittest.main()