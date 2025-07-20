# Write a program to accept a number from the user and check whether it's prime or not. If user enters anything other than number, handle the exception and print an error message. 
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError:
    print("Invalid input")