import unittest

from level2.JadenCase문자열만들기 import MakeJadenCase


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        s = "3people unFollowed me"
        expected = "3people Unfollowed Me"
        self.assertEqual(expected, MakeJadenCase.solution(s))  # add assertion here

    def test_case_two(self):
        s = "for the last week"
        expected = "For The Last Week"
        self.assertEqual(expected, MakeJadenCase.solution(s))

    def test_case_three(self):
        s = "for the last week"
        expected = "For The Last Week"
        self.assertEqual(expected, MakeJadenCase.solution_with_title(s))

    def test_case_four(self):
        s = "for the last week"
        expected = "For The Last Week"
        self.assertEqual(expected, MakeJadenCase.solution_with_title(s))


if __name__ == '__main__':
    unittest.main()
