class NextBiggerNumber:
    @staticmethod
    def solution(n: int) -> int:
        answer = n + 1
        n_binary_one_count = bin(n).count("1")

        while n_binary_one_count != bin(answer).count("1"):
            answer += 1

        return answer
