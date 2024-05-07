import unittest

from level2.숫자의표현 import NumberRepresentation


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        n = 15
        expected = 4
        self.assertEqual(expected, NumberRepresentation.solution(n))  # add assertion here

    def test_case_two(self):
        n = 1
        expected = 1
        self.assertEqual(expected, NumberRepresentation.solution(n))


if __name__ == '__main__':
    unittest.main()
