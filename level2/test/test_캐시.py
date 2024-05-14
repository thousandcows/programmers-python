import unittest

from level2.캐시 import Cache


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        cache_size = 3
        cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
        expected = 50
        self.assertEqual(expected, Cache.solution(cache_size, cities))  # add assertion here

    def test_case_two(self):
        cache_size = 3
        cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
        expected = 21
        self.assertEqual(expected, Cache.solution(cache_size, cities))

    def test_case_three(self):
        cache_size = 2
        cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju",
                  "NewYork", "Rome"]
        expected = 60
        self.assertEqual(expected, Cache.solution(cache_size, cities))

    def test_case_four(self):
        cache_size = 5
        cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju",
                  "NewYork", "Rome"]
        expected = 52
        self.assertEqual(expected, Cache.solution(cache_size, cities))

    def test_case_five(self):
        cache_size = 2
        cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
        expected = 16
        self.assertEqual(expected, Cache.solution(cache_size, cities))

    def test_case_six(self):
        cache_size = 0
        cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
        expected = 25
        self.assertEqual(expected, Cache.solution(cache_size, cities))


if __name__ == '__main__':
    unittest.main()
