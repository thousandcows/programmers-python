import re
from collections import OrderedDict


class SortFileName:
    @staticmethod
    def solution(files: list[str]) -> list[str]:
        files = sorted(files, key=lambda file: int(re.findall(r'\d+', file)[0]))
        return sorted(files, key=lambda file: re.split("\d+", file.lower())[0])
