import unittest

from level2.점프와순간이동 import JumpAndTeleport


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        n = 5
        expected = 2
        self.assertEqual(expected, JumpAndTeleport.solution(n))  # add assertion here

    def test_case_two(self):
        n = 6
        expected = 2
        self.assertEqual(expected, JumpAndTeleport.solution(n))

    def test_case_three(self):
        n = 5000
        expected = 5
        self.assertEqual(expected, JumpAndTeleport.solution(n))


if __name__ == '__main__':
    unittest.main()
