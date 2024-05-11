from collections import Counter


class Discount:
    @staticmethod
    def solution(want: list[str], number: list[int], discount: list[str]) -> int:

        def check_wishlist_and_cart() -> int:
            nonlocal want, wishlist_dict, daily_cart_dict
            for w in want:
                if wishlist_dict[w] != daily_cart_dict.get(w, 0):
                    return 0
            return 1

        answer = 0
        total_products_count = sum(number)
        wishlist_dict = {product: count for product, count in zip(want, number)}
        daily_cart_dict = dict(Counter(discount[:total_products_count]))

        for day in range(total_products_count, len(discount)):

            answer += check_wishlist_and_cart()

            daily_cart_dict[discount[day - total_products_count]] -= 1
            if discount[day] in daily_cart_dict:
                daily_cart_dict[discount[day]] += 1
            else:
                daily_cart_dict[discount[day]] = 1
        answer += check_wishlist_and_cart()
        return answer
