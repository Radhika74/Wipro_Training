# Q3. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57

def same_last_digit(a,b):
    if a%10 == b%10:
        return True
    else:
        return False

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(same_last_digit(a,b))