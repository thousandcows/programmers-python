from collections import deque


class RotateParenthesis:
    @staticmethod
    def solution(s: str) -> int:
        def increment_answer_if_is_valid_string():
            nonlocal answer, q, pairs_dict
            stack = []
            for char in q:
                if stack and char in pairs_dict and pairs_dict[char] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)

            if not stack:
                answer += 1

        answer = 0
        q = deque(s)
        pairs_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for _ in range(len(s)):
            increment_answer_if_is_valid_string()
            q.append(q.popleft())

        return answer
