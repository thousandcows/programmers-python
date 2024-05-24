import unittest

from level2.큰수만들기 import MakeBigNumber


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        number = "1924"
        k = 2
        expected = "94"
        self.assertEqual(
            expected, MakeBigNumber.solution(number, k)
        )  # add assertion here

    def test_case_two(self):
        number = "1231234"
        k = 3
        expected = "3234"
        self.assertEqual(expected, MakeBigNumber.solution(number, k))

    def test_case_three(self):
        number = "4177252841"
        k = 4
        expected = "775841"
        self.assertEqual(expected, MakeBigNumber.solution(number, k))


if __name__ == "__main__":
    unittest.main()
