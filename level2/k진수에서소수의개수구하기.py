class FindPrimeNumberInK:
    @staticmethod
    def solution(n: int, k: int) -> int:
        def is_prime_number(num: str) -> bool:

            if not num:
                return False

            num = int(num)
            if num == 1:
                return False

            for i in range(2, int(num**0.5)):
                if num % i == 0:
                    return False
            return True

        answer = 0
        converted_number = ""
        if k != 10:
            while n > k:
                converted_number += str(n % k)
                n //= k
            converted_number += str(n)
        else:
            converted_number = str(n)

        for number in converted_number[::-1].split("0"):
            if is_prime_number(number):
                answer += 1

        return answer
