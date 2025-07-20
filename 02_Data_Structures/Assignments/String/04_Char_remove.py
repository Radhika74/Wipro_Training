# Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi".
def str_fun(s):
    if s.startswith('x'):
        s = s[1:]
    if s.endswith('x'):
        s = s[:-1]
    return s

str = input("Enter any string: ")
print(str_fun(str))