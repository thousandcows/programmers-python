import unittest

from level2.압축 import Compression


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        msg = "KAKAO"
        expected = [11, 1, 27, 15]
        self.assertEqual(expected, Compression.solution(msg))  # add assertion here

    def test_case_two(self):
        msg = "TOBEORNOTTOBEORTOBEORNOT"
        expected = [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
        self.assertEqual(expected, Compression.solution(msg))

    def test_case_three(self):
        msg = "ABABABABABABABAB"
        expected = [1, 2, 27, 29, 28, 31, 30]
        self.assertEqual(expected, Compression.solution(msg))


if __name__ == "__main__":
    unittest.main()
