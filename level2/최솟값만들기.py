class MakeMinValue:
    @staticmethod
    def solution(a: list[int], b: list[int]) -> int:
        return sum([one * two for one, two in zip(sorted(a), sorted(b, reverse=True))])
