def is_armstrong_number(num):
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num
a = int(input("Enter a number: "))

if is_armstrong_number(a):
    print(f"{a} is an Armstrong number.")
else:
    print(f"{a} is not an Armstrong number.")