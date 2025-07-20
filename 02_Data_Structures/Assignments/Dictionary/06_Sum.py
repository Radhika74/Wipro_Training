# Write a program to sum all the values in a dictionary, considering the values will be of int type.
data_dict = {}
n = int(input("Enter the number of entries: "))

for _ in range(n):
  key = int(input("Enter key: "))
  value = int(input("Enter value: "))
  data_dict[key] = value
print(data_dict)
sum=0
for value in data_dict.values():
    sum+=value
print(sum)
