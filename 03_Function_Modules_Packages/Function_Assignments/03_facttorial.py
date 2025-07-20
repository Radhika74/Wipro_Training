# Write a function to calculate and return the factorial of a number (a non-negative integer).
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(int(input("Enter a number: "))))
