# Write a program to check whether an element exists in a tuple or not.
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
element = int(input("Enter an element to check if it exists in the tuple or not: "))
if element in tup:
    print("Element exists in the tuple")
else:
    print("Element does not exist in the tuple")
