import unittest

from level2.튜플 import Tuple


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
        expected = [2, 1, 3, 4]
        self.assertEqual(expected, Tuple.solution(s))  # add assertion here

    def test_case_two(self):
        s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
        expected = [2, 1, 3, 4]
        self.assertEqual(expected, Tuple.solution(s))

    def test_case_three(self):
        s = "{{20,111},{111}}"
        expected = [111, 20]
        self.assertEqual(expected, Tuple.solution(s))

    def test_case_four(self):
        s = "{{123}}"
        expected = [123]
        self.assertEqual(expected, Tuple.solution(s))

    def test_case_five(self):
        s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
        expected = [3, 2, 4, 1]
        self.assertEqual(expected, Tuple.solution(s))


if __name__ == '__main__':
    unittest.main()
