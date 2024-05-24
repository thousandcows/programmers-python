import unittest

from level2.더맵게 import Spicier


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        scoville = [1, 2, 3, 9, 10, 12]
        k = 7
        expected = 2
        self.assertEqual(expected, Spicier.solution(scoville, k))  # add assertion here


if __name__ == '__main__':
    unittest.main()
