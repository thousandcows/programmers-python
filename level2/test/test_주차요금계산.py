import unittest

from level2.주차요금계산 import ParkingFeeCalculator


class MyTestCase(unittest.TestCase):
    def test_case_one(self):
        fees = [180, 5000, 10, 600]
        records = [
            "05:34 5961 IN",
            "06:00 0000 IN",
            "06:34 0000 OUT",
            "07:59 5961 OUT",
            "07:59 0148 IN",
            "18:59 0000 IN",
            "19:09 0148 OUT",
            "22:59 5961 IN",
            "23:00 5961 OUT",
        ]
        expected = [14600, 34400, 5000]
        self.assertEqual(
            expected, ParkingFeeCalculator.solution(fees, records)
        )  # add assertion here

    def test_case_two(self):
        fees = [120, 0, 60, 591]
        records = [
            "16:00 3961 IN",
            "16:00 0202 IN",
            "18:00 3961 OUT",
            "18:00 0202 OUT",
            "23:58 3961 IN",
        ]
        expected = [0, 591]
        self.assertEqual(expected, ParkingFeeCalculator.solution(fees, records))

    def test_case_three(self):
        fees = [1, 461, 1, 10]
        records = [
            "00:00 1234 IN",
        ]
        expected = [14841]
        self.assertEqual(expected, ParkingFeeCalculator.solution(fees, records))


if __name__ == "__main__":
    unittest.main()
