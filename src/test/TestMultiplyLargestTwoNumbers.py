import unittest
from src.main.FindLargestTwoNumbers import multiplyLargestTwoNumbers

class TestMultiplyLargestTwoNumbers(unittest.TestCase):

    def test1(self):
        result = multiplyLargestTwoNumbers(3, 2, 1)
        self.assertEqual(6, result)

    def test2(self):
        result = multiplyLargestTwoNumbers(7, 0, 4)
        self.assertEqual(28, result)

    def test3(self):
        result = multiplyLargestTwoNumbers(-4, 0.5, -3)
        self.assertEqual(-1.5, result)

    def test4(self):
        result = multiplyLargestTwoNumbers(3, 3, 3)
        self.assertEqual(9, result)

if __name__ == '__main__':
    unittest.main()
