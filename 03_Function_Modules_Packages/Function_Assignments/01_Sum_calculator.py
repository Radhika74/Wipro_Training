# Write a function to return the sum of all numbers in a list.
# Sample List: (8, 2, 3, 0, 7)
# Expected Output: 20
def sum_list(list1):
    return sum(list1)

print("Enter list value separated by space: ")
list1 = list(map(int, input().split()))
print(sum_list(list1))
