class RotateParenthesis:
    @staticmethod
    def solution(s: str) -> int:
        def is_valid_string(sub_str: str):
            nonlocal answer
            pairs_dict = {
                ")": "(",
                "]": "[",
                "}": "{"
            }
            stack = []
            for char in sub_str:
                if stack and char in pairs_dict and pairs_dict[char] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(char)
            return not stack

        answer = 0
        s = s * 2
        for idx in range(len(s) // 2):
            if is_valid_string(
                    s[idx: idx + len(s) // 2]
            ):
                answer += 1

        return answer
