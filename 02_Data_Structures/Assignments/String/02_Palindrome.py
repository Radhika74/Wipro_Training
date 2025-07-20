# Write a program that will check whether a given String is Palindrome or not.
str = input("Enter any string: ")
if str == str[::-1]:
    print("String is palindrome")
else:
    print("String is not palindrome")
