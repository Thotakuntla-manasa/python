from prime import is_prime
def print_primes_in_interval(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)
start = 10
end = 50
print(f"Prime numbers between {start} and {end} are:")
print_primes_in_interval(start, end)