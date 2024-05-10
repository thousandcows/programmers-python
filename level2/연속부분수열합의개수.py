class CountSubsequenceSum:
    @staticmethod
    def solution(elements: list[int]) -> int:
        answer = set()
        for i in range(1, len(elements) + 1):
            for idx, num in enumerate(elements):
                counter, curr_idx, curr_total = 0, idx, 0
                while counter < i:
                    if curr_idx > len(elements) - 1:
                        curr_idx = 0
                    curr_total += elements[curr_idx]
                    counter, curr_idx = counter + 1, curr_idx + 1
                answer.add(curr_total)
        return len(answer)
