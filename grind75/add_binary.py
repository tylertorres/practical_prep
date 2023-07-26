from collections import deque
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_converted = convert_to_decimal(a)
        b_converted = convert_to_decimal(b)

        return convert_to_binary(a_converted + b_converted)

def convert_to_decimal(binary_string: str):
    converted_number = 0
    n = len(binary_string)

    for i in range(n, 0, -1):
        print(binary_string[n - i])
        if binary_string[n - i] == '1':
            converted_number = converted_number + 2**(i - 1)

    return converted_number

def convert_to_binary(number: int):
    converted = deque()

    while number != 0 or len(converted) == 0:
        converted.appendleft(str(number % 2))
        number //= 2

    return "".join(converted)
