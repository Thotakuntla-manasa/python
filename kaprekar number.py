def is_kaprekar_number(n):
    if n < 1:
        return False
    square_str = str(n ** 2)
    left, right = square_str[:-len(str(n))] or "0", square_str[-len(str(n)):]
    return int(left) + int(right) == n

if __name__ == "__main__":
    num = int(input("Enter a number to check if it is a Kaprekar number: "))
    if is_kaprekar_number(num):
        print(f"{num} is a Kaprekar number.")
    else:
        print(f"{num} is not a Kaprekar number.")