#Unit testing in Python is a fundamental aspect
# of ensuring the reliability
# and correctness of your code.
# It involves testing individual units or components of a software application to verify that each unit performs as expected. Python provides a built-in module called unittest that facilitates the implementation of unit tests.
import unittest


# A simple function to be tested
def add(a, b): # type: ignore
    return a + b # type: ignore


# A class inheriting from unittest.TestCase
class TestAddFunction(unittest.TestCase):

    # Define test cases using methods that start with "test_"
    def test_add_positive_numbers(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)


# Run the tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()
