# Write a function that takes a number as a parameter and checks whether the number is prime or not.
def prime_checker(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
    
num = int(input("Enter a number: "))
print(prime_checker(num))
