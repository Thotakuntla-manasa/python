import math
def is_sunny_number(num):
    next_num = num + 1
    sqrt_next_num = math.sqrt(next_num)
    return sqrt_next_num.is_integer()
n = int(input("Enter a number: "))
if is_sunny_number(n):
    print(f"{n} is a Sunny number.")
else:
    print(f"{n} is not a Sunny number.")