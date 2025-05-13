def is_disarium_number(num):
    num_str = str(num)
    total = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    return total == num
a = int(input("Enter a number: "))
if is_disarium_number(a):
    print(f"{a} is a Disarium number.")
else:
    print(f"{a} is not a Disarium number.")