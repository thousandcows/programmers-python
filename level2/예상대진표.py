class Tournament:
    @staticmethod
    def solution(n: int, a: int, b: int) -> int:
        round_counter = 0
        while a != b:
            a, b = (a + 1) // 2, (b + 1) // 2
            round_counter += 1

        return round_counter
