class MaxMin:
    @staticmethod
    def solution(s: str) -> str:
        s = list(map(int, s.split()))
        return f'{min(s)} {max(s)}'
