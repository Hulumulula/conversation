import unittest
from main import calculate


class Task2TestCase(unittest.TestCase):
    def test_1(self):
        result = calculate(3, 3, [6, 2, 3])
        self.assertEqual(result, 12)

    def test_2(self):
        result = calculate(3, 3, [2, 4, 8])
        self.assertEqual(result, 14)

    def test_3(self):
        result = calculate(5, 4, [5, 2, 1, 7])
        self.assertEqual(result, 20)

    def test_4(self):
        result = calculate(5, 4, [5, 7, 1, 1])
        self.assertEqual(result, 24)

    def test_5(self):
        result = calculate(15, 10, [5, 7, 1, 1, 12, 5, 1, 2, 8, 6])
        self.assertEqual(result, 74)

    def test_6(self):
        result = calculate(13, 4, [10, 1, 9, 2])
        self.assertEqual(result, 76)


if __name__ == '__main__':
    unittest.main()
