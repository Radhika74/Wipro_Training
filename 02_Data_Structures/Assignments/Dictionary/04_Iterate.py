# Write a program to iterate over a dictionary using for loop and print the keys alone, values alone, and both keys and values.
dict={0:10,1:20,2:30}
for key in dict:
    print(key)
for value in dict:
    print(value)
for key,value in dict.items():
    print(key,value)
