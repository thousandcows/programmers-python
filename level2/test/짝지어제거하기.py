class DeletePairs:
    @staticmethod
    def solution(s: str) -> int:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return 1 if not stack else 0
