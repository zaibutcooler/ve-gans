# test_demo.py
import unittest

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b



class TestDemoFunctions(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        # Add more test cases as needed

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(-1, 1), -1)
        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()