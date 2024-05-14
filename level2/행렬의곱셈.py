class MatrixMultiplication:
    @staticmethod
    def solution(arr1: list[list[int]], arr2: list[list[int]]):
        answer = [[] for _ in range(len(arr1))]
        for row_num, row in enumerate(arr1):
            for col in list(zip(*arr2)):
                answer[row_num].append(sum([a * b for a, b in zip(row, col)]))
        return answer
