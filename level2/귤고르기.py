from collections import Counter


class ChooseTangerine:
    @staticmethod
    def solution(k: int, tangerine: list[int]) -> int:
        tangerine_value_list = sorted(list(Counter(tangerine).values()), reverse=True)

        tangerine_box, kind = 0, 0
        for count in tangerine_value_list:
            if tangerine_box >= k:
                break
            tangerine_box += count
            kind += 1

        return kind
