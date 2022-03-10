import unittest
from main import analyse


class Task1TestCase(unittest.TestCase):
    def test_1(self):
        result = analyse([('принять', 1),('принять', 2),('выгрузить', 1),('принять', 3),('принять', 4),('выгрузить', 3)])
        self.assertEqual(result, 6)

    def test_2(self):
        result = analyse([('принять', 1),('принять', 2),('принять', 3),('принять', 4),('выгрузить', 2),('принять', 5),('принять', 6),('выгрузить', 1),('принять', 7),('выгрузить', 5)])
        self.assertEqual(result, 12)

    def test_3(self):
        result = analyse([('принять', 46),('выгрузить', 46),('принять', 21),('выгрузить', 21)])
        self.assertEqual(result, 4)

    def test_4(self):
        result = analyse([('принять', 10),('принять', 12),('принять', 30),('принять', 15),('принять', 17),('выгрузить', 12),('выгрузить', 15),('выгрузить', 30),('принять', 50),('принять', 51),('выгрузить', 17),('выгрузить', 50),('выгрузить', 51),('выгрузить', 10)])
        self.assertEqual(result, 24)

if __name__ == '__main__':
    unittest.main()
