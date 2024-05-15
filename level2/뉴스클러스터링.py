import re
from collections import Counter


class NewsClustering:
    @staticmethod
    def solution(str1: str, str2: str) -> int:
        str1, str2 = str1.lower(), str2.lower()
        str1_counter = Counter([str1[i : i + 2] for i in range(len(str1) - 1)])
        str2_counter = Counter([str2[i : i + 2] for i in range(len(str2) - 1)])

        str1_counter_keys = set(
            [
                key
                for key in str1_counter.keys()
                if len(re.sub(r"[^a-z,A-Z]", "", key)) == 2
            ]
        )

        str2_counter_keys = set(
            [
                key
                for key in str2_counter.keys()
                if len(re.sub(r"[^a-z,A-Z]", "", key)) == 2
            ]
        )

        intersection_set, union_set = (
            str1_counter_keys & str2_counter_keys,
            str1_counter_keys | str2_counter_keys,
        )

        intersection_count = sum(
            min(str1_counter[key], str2_counter[key]) for key in intersection_set
        )
        union_count = sum(
            max(str1_counter[key], str2_counter[key]) for key in union_set
        )

        if intersection_count == union_count:
            return 65536

        return int(intersection_count / union_count * 65536)
