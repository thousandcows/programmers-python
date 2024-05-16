import unittest

from level2.롤케이크자르기 import CutRollCake


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        topping = [1, 2, 1, 3, 1, 4, 1, 2]
        expected = 2
        self.assertEqual(CutRollCake.solution(topping), expected)  # add assertion here

    def test_case_two(self):
        topping = [1, 2, 3, 1, 4]
        expected = 0
        self.assertEqual(CutRollCake.solution(topping), expected)


if __name__ == "__main__":
    unittest.main()
