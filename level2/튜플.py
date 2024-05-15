from collections import Counter


class Tuple:
    @staticmethod
    def solution(s: str) -> list[int]:
        return [
            element[0]
            for element in sorted(
                Counter(
                    list(map(int, s.replace("{", "").replace("}", "").split(",")))
                ).items(),
                reverse=True,
                key=lambda x: x[1],
            )
        ]
