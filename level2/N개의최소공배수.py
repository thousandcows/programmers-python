class NLcm:
    @staticmethod
    def solution(arr: list[int]) -> int:

        def find_lcm(a: int, b: int):
            if max(a, b) % min(a, b) == 0:
                return max(a, b)
            lcm = 1
            for n in range(min(a, b) + 1, 1, -1):
                if a % n == 0 and b % n == 0:
                    lcm, a, b = lcm * n, a // n, b // n
            return lcm * a * b

        answer = 1
        for idx in range(0, len(arr)):
            answer = find_lcm(answer, arr[idx])

        return answer
