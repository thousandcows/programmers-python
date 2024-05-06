class MakeJadenCase:
    @staticmethod
    def solution(s: str) -> str:
        return ' '.join([word.capitalize() for word in s.split(' ')])

    @staticmethod
    def solution_with_title(s: str) -> str:
        return s.title()
