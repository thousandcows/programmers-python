class JumpAndTeleport:
    @staticmethod
    def solution(n: int) -> int:
        memoization = [0, 1, 1, 2]
        for i in range(4, n + 1):
            if i % 2 == 0:
                memoization.append(min(memoization[i // 2], memoization[i - 1] + 1))
            else:
                memoization.append(memoization[i - 1] + 1)

        return memoization[n]
