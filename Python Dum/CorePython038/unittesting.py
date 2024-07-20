import unittest
from function_programs import msg, add, addition

class TestFunctionPrograms(unittest.TestCase):
    def test_msg(self):
        self.assertEqual(msg(), 'hello all')

    def test_add(self):
        self.assertEqual(add(30, 20), 50)
        self.assertEqual(add(b=40, a=30), 70)
        self.assertEqual(add(10, 20), 30)

    def test_addition(self):
        self.assertEqual(addition(20, 30, 40), 90)
        self.assertEqual(addition(1, 2, 3, 4, 5), 15)
        self.assertEqual(addition(*[12, 13, 14, 15, 16]), 70)
        self.assertEqual(addition(30, 40), 70)

if __name__ == '__main__':
    unittest.main()
