# Write a function to print the even numbers from a given list. List is passed to the function as an argument.
# Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result: [2, 4, 6, 8]
def filter_num(list):
    for i in list:
        if i%2==0:
            print(i)

list1 = list(map(int, input().split()))
filter_num(list1)
