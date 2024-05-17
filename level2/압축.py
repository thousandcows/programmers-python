import string


class Compression:
    @staticmethod
    def solution(msg: str) -> list[int]:
        answer = []
        dictionary = {alpha: idx for idx, alpha in enumerate(string.ascii_uppercase, 1)}

        curr_index, dict_end_index = 0, 27

        curr_word = ""
        while curr_index < len(msg):
            curr_word += msg[curr_index]
            if curr_word in dictionary:
                curr_index += 1
                continue

            answer.append(dictionary[curr_word[:-1]])
            dictionary[curr_word] = dict_end_index
            dict_end_index += 1
            curr_word = ""
        answer.append(dictionary[curr_word])

        return answer
