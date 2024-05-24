import unittest

from level2.숫자변환하기 import TransformNumber


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        x = 10
        y = 40
        n = 5
        expected = 2
        self.assertEqual(expected, TransformNumber.solution(x, y, n))  # add assertion here

    def test_case_two(self):
        x = 10
        y = 40
        n = 30
        expected = 1
        self.assertEqual(expected, TransformNumber.solution(x, y, n))

    def test_case_three(self):
        x = 2
        y = 5
        n = 4
        expected = -1
        self.assertEqual(expected, TransformNumber.solution(x, y, n))

if __name__ == '__main__':
    unittest.main()
