import unittest

from level2.구명보트 import Boat


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        people = [70, 50, 80, 50]
        limit = 100
        expected = 3
        self.assertEqual(expected, Boat.solution(people, limit))  # add assertion here

    def test_case_two(self):
        people = [70, 80, 50]
        limit = 100
        expected = 3
        self.assertEqual(expected, Boat.solution(people, limit))

    def test_case_three(self):
        people = [40, 70, 100, 100]
        limit = 100
        expected = 4
        self.assertEqual(expected, Boat.solution(people, limit))

    def test_case_four(self):
        people = [40, 80, 60, 190, 210, 200]
        limit = 240
        expected = 4
        self.assertEqual(expected, Boat.solution(people, limit))

    def test_case_five(self):
        people = [40, 40, 40, 40, 40, 40, 40, 40, 40, 40]
        limit = 240
        expected = 5
        self.assertEqual(expected, Boat.solution(people, limit))


if __name__ == '__main__':
    unittest.main()
