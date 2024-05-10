import unittest

from level2.귤고르기 import ChooseTangerine


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        k = 6
        tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
        expected = 3
        self.assertEqual(expected, ChooseTangerine.solution(k, tangerine))  # add assertion here

    def test_case_two(self):
        k = 4
        tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
        expected = 2
        self.assertEqual(expected, ChooseTangerine.solution(k, tangerine))

    def test_case_three(self):
        k = 2
        tangerine = [1, 1, 1, 1, 2, 2, 2, 3]
        expected = 1
        self.assertEqual(expected, ChooseTangerine.solution(k, tangerine))


if __name__ == '__main__':
    unittest.main()
