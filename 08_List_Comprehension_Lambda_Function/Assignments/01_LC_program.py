# Write a LC program to create an output dictionary which contains only the odd numbers that are present in the input list = [1,2,3,4,5,6,7] as keys and their cubes as values

list1 =[1, 2, 3, 4, 5, 6, 7]
output ={x: x**3 for x in list1 if x % 2 != 0}
print(output)