class JumpJump:
    @staticmethod
    def solution(n: int) -> int:
        if n <= 2:
            return 2 if n == 2 else 1

        first, second, counter = 1, 2, 3
        while counter <= n:
            first, second = second, (first + second) % 1234567
            counter += 1

        return second
