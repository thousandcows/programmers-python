import unittest

from level2.멀리뛰기 import JumpJump


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        n = 4
        expected = 5
        self.assertEqual(expected, JumpJump.solution(n))  # add assertion here

    def test_case_two(self):
        n = 3
        expected = 3
        self.assertEqual(expected, JumpJump.solution(n))


if __name__ == '__main__':
    unittest.main()
