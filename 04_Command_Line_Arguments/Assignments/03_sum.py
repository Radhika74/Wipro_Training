# Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them
import sys
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

if len(sys.argv) != 11:
    print("Usage: python sum_of_primes.py <10 numbers>")
    sys.exit(1)

numbers = list(map(int, sys.argv[1:]))
prime_sum = sum(num for num in numbers if is_prime(num))
print(f"Sum of prime numbers: {prime_sum}")
