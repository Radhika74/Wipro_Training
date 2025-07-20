# Write a program to find the index of an item in a tuple.
def find_ele(tup, element):
    if element in tup:
        for i in range(len(tup)):
            if tup[i] == element:
                return i
    return -1
elements = input("Enter tuple elements separated by space: ")
tup = tuple(map(int, elements.split()))
element = int(input("Enter an element to find its index: "))

result = find_ele(tup, element)
if result != -1:
    print(f"Item {element} found at index {result}.")
else:
    print(f"Item {element} not found in the tuple.")
