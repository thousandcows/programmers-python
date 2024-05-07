class NumberRepresentation:
    @staticmethod
    def solution(n: int) -> int:
        answer = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if i >= n:
                    break
                i += j
            if i == n:
                answer += 1
        return answer
