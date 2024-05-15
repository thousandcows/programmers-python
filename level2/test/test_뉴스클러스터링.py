import unittest

from level2.뉴스클러스터링 import NewsClustering


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        str1 = "FRANCE"
        str2 = "french"
        expected = 16384
        self.assertEqual(
            expected, NewsClustering.solution(str1, str2)
        )  # add assertion here

    def test_case_two(self):
        str1 = "handshake"
        str2 = "shake hands"
        expected = 65536
        self.assertEqual(expected, NewsClustering.solution(str1, str2))

    def test_case_three(self):
        str1 = "aa1+aa2"
        str2 = "AAAA12"
        expected = 43690
        self.assertEqual(expected, NewsClustering.solution(str1, str2))

    def test_case_four(self):
        str1 = "E=M*C^2"
        str2 = "e=m*c^2"
        expected = 65536
        self.assertEqual(expected, NewsClustering.solution(str1, str2))

    def test_case_five(self):
        str1 = "a"
        str2 = "a"
        expected = 65536
        self.assertEqual(expected, NewsClustering.solution(str1, str2))


if __name__ == "__main__":
    unittest.main()
