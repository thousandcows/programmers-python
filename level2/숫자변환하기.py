from collections import deque, defaultdict


class TransformNumber:
    @staticmethod
    def solution(x: int, y: int, n: int) -> int:

        answer = float('inf')

        q = deque([(x, 0)])
        visited = defaultdict(bool)
        found_the_answer = False

        while q:
            number, count = q.popleft()

            if number > y:
                continue

            if number == y:
                answer = min(count, answer)
                found_the_answer = True

            for next_number in [number + n, number * 2, number * 3]:
                if next_number <= y and not visited[next_number]:
                    q.append((next_number, count + 1))
                    visited[next_number] = True

        return answer if found_the_answer else -1
