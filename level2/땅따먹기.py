class ConquerTheLand:
    @staticmethod
    def solution(land: list[list[int]]) -> int:
        def dfs(row_num: int, col_num: int, total: int):
            nonlocal land, answer

            total += land[row_num][col_num]
            if row_num == len(land) - 1:
                answer = max(answer, total)
                return

            for new_col_num in range(4):
                if new_col_num == col_num:
                    continue
                dfs(row_num + 1, new_col_num, total)

        answer = 0
        for start_col in range(4):
            dfs(0, start_col, 0)

        return answer
