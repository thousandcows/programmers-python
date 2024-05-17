class FindPrimeNumberInK:
    @staticmethod
    def solution(n: int, k: int) -> int:
        def convert_to_digit_ten(digit, target_num):
            if digit == 10:
                return str(target_num)

            result = ""
            while target_num != 0:
                result += str(target_num % digit)
                target_num //= digit
            result += str(target_num)
            return result[::-1]

        def is_prime_number(num: int) -> bool:
            num = int(num)
            if num == 1:
                return False

            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        answer = 0
        converted_number = convert_to_digit_ten(k, n)
        for number in converted_number.split("0"):

            if not number:
                continue

            if is_prime_number(int(number)):
                answer += 1

        return answer
