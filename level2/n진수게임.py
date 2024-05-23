class NDigitGame:
    @staticmethod
    def solution(n: int, t: int, m: int, p: int) -> str:
        helper_dictionary = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

        def transform_number(digit: int, target_number: int):
            result = ""

            while target_number != 0:
                curr_number = target_number % digit
                if curr_number in helper_dictionary:
                    result += helper_dictionary[curr_number]
                else:
                    result += str(curr_number)

                target_number //= digit
            return result[::-1]

        game_string = "001"

        number = 2
        while len(game_string) <= p + (m * t):
            game_string += transform_number(n, number)
            number += 1

        return "".join([game_string[i] for i in range(p, len(game_string), m)])[:t]
