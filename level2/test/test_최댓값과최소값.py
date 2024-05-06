import unittest

from level2.최댓값과최솟값 import MaxMin


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        s = "1 2 3 4"
        expected = "1 4"
        self.assertEqual(expected, MaxMin.solution(s))  # add assertion here

    def test_case_two(self):
        s = "-1 -2 -3 -4"
        expected = "-4 -1"
        self.assertEqual(expected, MaxMin.solution(s))

    def test_case_three(self):
        s = "-1 -1"
        expected = "-1 -1"
        self.assertEqual(expected, MaxMin.solution(s))


if __name__ == '__main__':
    unittest.main()
