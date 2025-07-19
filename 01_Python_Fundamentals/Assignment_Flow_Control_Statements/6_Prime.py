# Q6. Write a program to check if a given number is prime or not.

def is_prime(n):
    if n <= 1:
        return f"{n} is not prime number"
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f"{n} is not prime number"
    
    return f"{n} is prime number"

n = int(input())
print(is_prime(n))
