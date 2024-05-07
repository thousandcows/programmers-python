import unittest

from level2.이진변환반복하기 import ConvertToBinary


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        s = "110010101001"
        expected = [3, 8]
        self.assertEqual(expected, ConvertToBinary.solution(s))  # add assertion here

    def test_case_two(self):
        s = "01110"
        expected = [3, 3]
        self.assertEqual(expected, ConvertToBinary.solution(s))

    def test_case_three(self):
        s = "1111111"
        expected = [4, 1]
        self.assertEqual(expected, ConvertToBinary.solution(s))


if __name__ == '__main__':
    unittest.main()
