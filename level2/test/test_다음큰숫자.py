import unittest

from level2.다음큰숫자 import NextBiggerNumber


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        n = 78
        expected = 83
        self.assertEqual(expected, NextBiggerNumber.solution(n))  # add assertion here

    def test_case_two(self):
        n = 15
        expected = 23
        self.assertEqual(expected, NextBiggerNumber.solution(n))


if __name__ == '__main__':
    unittest.main()
