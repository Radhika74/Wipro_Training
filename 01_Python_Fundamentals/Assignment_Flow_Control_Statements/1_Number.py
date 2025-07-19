# Q1. Write a program to check if a given number is Positive, Negative or Zero.

def check_negative_positive(a):
    if a>0:
        print("Positive")
    elif a==0:
        print("Zero")
    else:
        print("Negative")

res = int(input("Enter a number: "))
check_negative_positive(res)