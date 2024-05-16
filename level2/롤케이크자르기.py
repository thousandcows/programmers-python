from collections import defaultdict, Counter


class CutRollCake:
    @staticmethod
    def solution(topping: list[int]) -> int:
        answer = 0
        left_dict, right_dict = defaultdict(int), dict(Counter(topping))

        for idx, top in enumerate(topping):
            if len(left_dict) == len(right_dict):
                answer += 1
            left_dict[top] += 1
            right_dict[top] -= 1

            if right_dict[top] <= 0:
                del right_dict[top]

        return answer
