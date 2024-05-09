class Boat:
    @staticmethod
    def solution(people: list[int], limit: int) -> int:
        left, right, escaped_together = 0, len(people) - 1, 0
        people.sort()

        while left < right:

            if people[left] + people[right] <= limit:
                escaped_together += 1
                left += 1

            right -= 1
        return len(people) - escaped_together
