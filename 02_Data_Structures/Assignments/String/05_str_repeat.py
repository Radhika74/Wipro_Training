# Given a string and an integer n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string inclusive. For example if the inputs are "Wipro" and 3, then the output should be "propropro".
def str_fun(s, n):
    return s[-n:]*n

s = input("Enter any string: ")
n = int(input("Enter any integer: "))
print(str_fun(s,n))