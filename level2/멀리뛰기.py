class JumpJump:
    @staticmethod
    def solution(n: int) -> int:
        if n <= 2:
            return 2 if n == 2 else 1

        arr = [0 for _ in range(n + 1)]
        arr[1], arr[2] = 1, 2

        idx = 3
        while idx <= n:
            arr[idx] = (arr[idx - 1] + arr[idx - 2]) % 1234567
            idx += 1

        return arr[n]
