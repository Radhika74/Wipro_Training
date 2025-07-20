# Write a program to print the number of occurrences of a specified element in a list.
list = []
for i in range(5):
    list.append(int(input("Enter an integer: ")))
print(list)
element = int(input("Enter an element to count: "))
print(list.count(element))
