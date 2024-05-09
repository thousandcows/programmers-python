class Tournament:
    @staticmethod
    def solution(n: int, a: int, b: int) -> int:
        round_counter = 1
        a, b = min(a, b), max(a, b)
        while abs(a - b) != 1 or a % 2 != 1 or b % 2 != 0:
            a = a // 2 if a % 2 == 0 else (a + 1) // 2
            b = b // 2 if b % 2 == 0 else (b + 1) // 2
            round_counter += 1

        return round_counter
