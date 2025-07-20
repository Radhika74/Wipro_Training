# Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result.
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
try:
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except Exception as e:
    print("An error occurred:", e)
