class JumpAndTeleport:

    @staticmethod
    def solution_with_bin(self, n: int) -> int:
        return bin(n).count('1')

    @staticmethod
    def solution(n: int) -> int:
        ans = 1
        while n > 1:
            ans += n % 2
            n = n // 2
        return ans
