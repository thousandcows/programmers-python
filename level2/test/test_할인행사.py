import unittest

from level2.할인행사 import Discount


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        want = ["banana", "apple", "rice", "pork", "pot"]
        number = [3, 2, 2, 2, 1]
        discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                    "banana", "apple", "banana"]
        expected = 3
        self.assertEqual(expected, Discount.solution(want, number, discount))  # add assertion here

    def test_case_two(self):
        want = ["apple"]
        number = [10]
        discount = ["banana"] * 10
        expected = 0
        self.assertEqual(expected, Discount.solution(want, number, discount))

    def test_case_three(self):
        want = ["pineapple", "banana"]
        number = [1, 1]
        discount = ["pineapple", "banana"]
        expected = 1
        self.assertEqual(expected, Discount.solution(want, number, discount))


if __name__ == '__main__':
    unittest.main()
