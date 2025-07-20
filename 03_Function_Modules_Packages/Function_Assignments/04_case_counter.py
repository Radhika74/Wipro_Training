# Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
def case_counter(string):
    upper=0
    lower=0
    for i in string:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print("Number of uppercase letters: ", upper)
    print("Number of lowercase letters: ", lower)

case_counter(input("Enter a string: "))