import unittest
from app import sum_function

class TestApp(unittest.TestCase):
    def test_sum(self):
        result = sum_function(5, 10)
        self.assertEqual(result, 15, "Should be 15")

    def test_negative_sum(self):
        result = sum_function(-5, -10)
        self.assertEqual(result, -15, "Should be -15")

if __name__ == '__main__':
    unittest.main()


import unittest
from app import sum_function  # Assuming sum_function is the function to test

class TestApp(unittest.TestCase):
    def test_negative_sum(self):
        result = sum_function(-5, -10)
        self.assertEqual(result, -15, "The sum of -5 and -10 should be -15")

if __name__ == '__main__':
    unittest.main()
