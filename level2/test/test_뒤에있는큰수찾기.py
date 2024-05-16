import unittest

from level2.뒤에있는큰수찾기 import FindBiggerNumber


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        numbers = [2, 3, 3, 5]
        expected = [3, 5, 5, -1]
        self.assertEqual(
            FindBiggerNumber.solution(numbers), expected
        )  # add assertion here

    def test_case_two(self):
        numbers = [9, 1, 5, 3, 6, 2]
        expected = [-1, 5, 6, 6, -1, -1]
        self.assertEqual(FindBiggerNumber.solution(numbers), expected)


if __name__ == "__main__":
    unittest.main()
