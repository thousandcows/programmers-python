import unittest

from level2.연속부분수열합의개수 import CountSubsequenceSum


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        elements = [7, 9, 1, 1, 4]
        expected = 18
        self.assertEqual(expected, CountSubsequenceSum.solution(elements))  # add assertion here


if __name__ == '__main__':
    unittest.main()
