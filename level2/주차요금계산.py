import math
from collections import defaultdict


class ParkingFeeCalculator:
    @staticmethod
    def solution(fees: list[int], records: list[str]) -> list[int]:
        def convert_time_to_min(curr_time: str):
            hour, minute = curr_time.split(":")
            return int(hour) * 60 + int(minute)

        def calculate_total_parking_fees(parking_record: list[int]):
            if len(parking_record) % 2 != 0:
                parking_record.append(23 * 60 + 59)

            over_time_to_charge = 0
            basic_hours, basic_fee, over_time, over_charge = fees
            for idx in range(1, len(parking_record), 2):
                over_time_to_charge += parking_record[idx] - parking_record[idx - 1]

            return (
                basic_fee
                + math.ceil(max(over_time_to_charge - basic_hours, 0) / over_time)
                * over_charge
            )

        answer, parking_lot = [], defaultdict(list)

        for record in records:
            times, car_number, _ = record.split()
            parking_lot[car_number].append(convert_time_to_min(times))

        return [
            calculate_total_parking_fees(parking_lot[car_number])
            for car_number in sorted(parking_lot.keys())
        ]
