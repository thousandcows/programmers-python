from collections import Counter


class Discount:
    @staticmethod
    def solution(want: list[str], number: list[int], discount: list[str]) -> int:
        answer = 0
        wishlist_dict = {product: count for product, count in zip(want, number)}
        for day in range(len(discount) - 9):
            answer += 1 if wishlist_dict == Counter(discount[day:day + 10]) else 0

        return answer
