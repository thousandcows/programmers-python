class FindBiggerNumber:
    @staticmethod
    def solution(numbers: list[int]) -> list[int]:
        answer = []

        for i, curr_num in enumerate(numbers):
            flag = False
            for next_idx in range(i + 1, len(numbers)):
                if numbers[next_idx] > curr_num:
                    answer.append(numbers[next_idx])
                    flag = True
                    break
            if not flag:
                answer.append(-1)
        return answer
