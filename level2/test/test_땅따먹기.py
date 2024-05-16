import unittest

from level2.땅따먹기 import ConquerTheLand


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
        expected = 16
        self.assertEqual(expected, ConquerTheLand.solution(land))  # add assertion here


if __name__ == "__main__":
    unittest.main()
