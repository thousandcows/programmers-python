class MakeBigNumber:
    @staticmethod
    def solution(number: str, k: int) -> str:
        start_index, counter = 0, len(number) - k
        word = ""
        while counter != 0:
            max_number = "0"
            for idx in range(start_index, len(number) - counter + 1):
                if number[idx] > max_number:
                    max_number = number[idx]
                    start_index = idx + 1
            word += max_number
            counter -= 1
        return word
