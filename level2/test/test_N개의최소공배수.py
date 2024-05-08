import unittest

from level2.N개의최소공배수 import NLcm


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        arr = [1, 2, 3, 4]
        expected = 12
        self.assertEqual(expected, NLcm.solution(arr))  # add assertion here

    def test_case_two(self):
        arr = [2, 6, 8, 14]
        expected = 168
        self.assertEqual(expected, NLcm.solution(arr))

    def test_case_three(self):
        arr = [2, 3, 5, 7]
        expected = 210
        self.assertEqual(expected, NLcm.solution(arr))

    def test_case_four(self):
        arr = [1]
        expected = 1
        self.assertEqual(expected, NLcm.solution(arr))

    def test_case_five(self):
        arr = [11, 7, 77]
        expected = 77
        self.assertEqual(expected, NLcm.solution(arr))


if __name__ == '__main__':
    unittest.main()
