import unittest

from level2.최솟값만들기 import MakeMinValue


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        a, b, = [1, 4, 2], [5, 4, 4]
        expected = 29
        self.assertEqual(expected, MakeMinValue.solution(a, b))  # add assertion here

    def test_case_two(self):
        a, b, = [1, 2], [3, 4]
        expected = 10
        self.assertEqual(expected, MakeMinValue.solution(a, b))

    def test_case_three(self):
        a, b = [i for i in range(1, 1001)], [i for i in range(1, 1001)]
        expected = 167167000
        self.assertEqual(expected, MakeMinValue.solution(a, b))


if __name__ == '__main__':
    unittest.main()
