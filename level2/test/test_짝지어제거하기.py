import unittest

from level2.test.짝지어제거하기 import DeletePairs


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        s = "aabbaccc"
        expected = 0
        self.assertEqual(expected, DeletePairs.solution(s))  # add assertion here

    def test_case_two(self):
        s = "aaccdd"
        expected = 1
        self.assertEqual(expected, DeletePairs.solution(s))

    def test_case_three(self):
        s = "abba"
        expected = 1
        self.assertEqual(expected, DeletePairs.solution(s))

    def test_case_four(self):
        s = "abab"
        expected = 0
        self.assertEqual(expected, DeletePairs.solution(s))


if __name__ == '__main__':
    unittest.main()
