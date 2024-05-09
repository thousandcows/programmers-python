import unittest

from level2.예상대진표 import Tournament


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        n, a, b = 8, 4, 7
        expected = 3
        self.assertEqual(expected, Tournament.solution(n, a, b))  # add assertion here

    def test_case_two(self):
        n, a, b = 2, 1, 2
        expected = 1
        self.assertEqual(expected, Tournament.solution(n, a, b))

    def test_case_three(self):
        n, a, b = 4, 1, 2
        expected = 1
        self.assertEqual(expected, Tournament.solution(n, a, b))

    def test_case_four(self):
        n, a, b = 4, 1, 3
        expected = 2
        self.assertEqual(expected, Tournament.solution(n, a, b))

    def test_case_five(self):
        n, a, b = 16, 8, 9
        expected = 4
        self.assertEqual(expected, Tournament.solution(n, a, b))


if __name__ == '__main__':
    unittest.main()
