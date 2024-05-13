import unittest

from level2.괄호회전하기 import RotateParenthesis


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        s = "[](){}"
        expected = 3
        self.assertEqual(expected, RotateParenthesis.solution(s))  # add assertion here

    def test_case_two(self):
        s = "}]()[{"
        expected = 2
        self.assertEqual(expected, RotateParenthesis.solution(s))

    def test_case_three(self):
        s = "[)(]"
        expected = 0
        self.assertEqual(expected, RotateParenthesis.solution(s))

    def test_case_four(self):
        s = "}}}"
        expected = 0
        self.assertEqual(expected, RotateParenthesis.solution(s))


if __name__ == '__main__':
    unittest.main()
