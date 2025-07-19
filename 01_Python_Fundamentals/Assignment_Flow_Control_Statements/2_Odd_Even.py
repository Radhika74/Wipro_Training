# Q2. Write a program to check if a given number is odd or even.

def check_odd_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        return "Odd"

res =int(input("Enter a number: "))
print(check_odd_even(res))