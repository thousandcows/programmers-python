import re
from collections import OrderedDict


class SortFileName:
    @staticmethod
    def solution(files: list[str]) -> list[str]:

        def parse_file_name_and_digit(file_name: str) -> tuple:
            alpha, digit, digit_search_index = "", "", 0

            for idx, ch in enumerate(file_name):
                if ch.isdigit():
                    digit_search_index = idx
                    break
                alpha += ch

            while digit_search_index < len(file_name) and file_name[digit_search_index].isdigit() is False:
                digit_search_index += 1

            while digit_search_index < len(file_name) and file_name[digit_search_index].isdigit():
                digit += file_name[digit_search_index]
                digit_search_index += 1

            return alpha.lower(), int(digit)

        files_dict = OrderedDict()
        for file in files:
            files_dict[file] = parse_file_name_and_digit(file)

        return sorted(files_dict, key=lambda x: (files_dict[x][0], files_dict[x][1]))
