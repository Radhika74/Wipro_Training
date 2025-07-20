# Write a program to count the number of upper and lower case letters in a String.
str = input("Enter any string: ")
upper = 0
lower = 0
for i in str:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print("Number of uppercase letters in string: ", upper)
print("Number of lowercase letters in string: ", lower)
