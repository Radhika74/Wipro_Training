# Write a program to find check if a string has only octal digits. Given string ['789', '123', '004']

def octal_digit(nums):
    for i in nums:
        if set(i).issubset({'0', '1', '2', '3', '4', '5', '6', '7'}):
            print(i, "has octal digits.")
        else:
            print(i, "does not have only octal digits.")

nums =['789', '123', '004']
octal_digit(nums)