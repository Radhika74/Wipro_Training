# Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string. The string length will be >=2.
# If input is "Wipro" then output should be "WiWiWiWiWi".
str = input("Enter any string: ")
n = len(str)
if n>=2:
    print(str[:2]*n)
else:
    print("String length should be >=2")