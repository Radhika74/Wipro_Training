# Write a program to append a new item to the end of the list.
list = []
#Take list input from user
for i in range(5):
    list.append(int(input("Enter an integer: ")))
print(list)
list.append(int(input("Enter an integer to add at last: ")))
print("List after append",list)

