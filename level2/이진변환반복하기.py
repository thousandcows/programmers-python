
class ConvertToBinary:
    @staticmethod
    def solution(s: str) -> list[int]:
        def convert_to_binary(num: int) -> str:
            binary = ""
            while num > 1:
                binary += str(num % 2)
                num //= 2
            binary += str(num)
            return binary[::-1]

        count, deleted_zeros = 0, 0

        while len(s) != 1:
            deleted_zeros += s.count("0")
            s = s.replace("0", "")
            s = convert_to_binary(len(s))
            count += 1

        return [count, deleted_zeros]
