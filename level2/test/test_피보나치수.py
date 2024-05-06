import unittest

from level2.피보나치수 import Fibonacci


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        n = 3
        expected = 2
        self.assertEqual(expected, Fibonacci.solution(n))  # add assertion here

    def test_case_two(self):
        n = 5
        expected = 5
        self.assertEqual(expected, Fibonacci.solution(n))


if __name__ == '__main__':
    unittest.main()
