
from heapq import heappop, heappush, heapify


class Spicier:
    @staticmethod
    def solution(scoville: list[int], k: int) -> int:
        answer = 0

        scoville.sort()
        heapify(scoville)

        if scoville[0] >= k:
            return answer

        while scoville[0] < k:
            if len(scoville) == 1:
                return -1

            heappush(scoville, heappop(scoville) + heappop(scoville) * 2)
            answer += 1

        return answer
