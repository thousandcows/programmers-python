class SumOfSequences:
    @staticmethod
    def solution(sequence: list[int], k: int) -> list[int]:
        answer = []
        left, right, sub_total = 0, 1, sequence[0] + sequence[1]

        while not (left == right == len(sequence) - 1):
            if sequence[left] == k:
                answer = [left, left]
                break

            if right == len(sequence) - 1 and left < right:
                sub_total -= sequence[left]
                left += 1

            if sub_total < k and right < len(sequence) - 1:
                right += 1
                sub_total += sequence[right]  # 합 갱신

            elif sub_total > k:
                sub_total -= sequence[left]  # 합 갱신
                left += 1

            elif sub_total == k:
                if not answer or (answer and right - left < answer[1] - answer[0]):
                    answer = [left, right]

                if right < len(sequence) - 1:
                    right += 1
                    sub_total += sequence[right]  # 합 갱신

        return answer
