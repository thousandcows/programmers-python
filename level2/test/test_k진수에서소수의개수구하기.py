import unittest

from level2.k진수에서소수의개수구하기 import FindPrimeNumberInK


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        n = 437674
        k = 3
        expected = 3
        self.assertEqual(
            expected, FindPrimeNumberInK.solution(n, k)
        )  # add assertion here

    def test_case_two(self):
        n = 110011
        k = 10
        expected = 2
        self.assertEqual(expected, FindPrimeNumberInK.solution(n, k))

    def test_case_three(self):
        n = 300
        k = 4
        expected = 1
        self.assertEqual(expected, FindPrimeNumberInK.solution(n, k))


if __name__ == "__main__":
    unittest.main()
