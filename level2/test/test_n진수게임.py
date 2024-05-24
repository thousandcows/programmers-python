import unittest

from level2.n진수게임 import NDigitGame


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        n, t, m, p = 2, 4, 2, 1
        expected = "0111"
        self.assertEqual(expected, NDigitGame.solution(n, t, m, p))  # add assertion here

    def test_case_two(self):
        n, t, m, p = 16, 16, 2, 1
        expected = "02468ACE11111111"
        self.assertEqual(expected, NDigitGame.solution(n, t, m, p))

    def test_case_three(self):
        n, t, m, p = 16, 16, 2, 2
        expected = "13579BDF01234567"
        self.assertEqual(expected, NDigitGame.solution(n, t, m, p))


if __name__ == '__main__':
    unittest.main()
