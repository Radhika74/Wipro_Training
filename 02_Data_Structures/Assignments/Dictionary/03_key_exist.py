# Write a program to check if a given key already exists in a dictionary.
dict={0:10,1:20,2:30}

key =int(input("Enter key to check if it exist or not: "))
if key in dict:
    print("Key is present in the dictionary")
else:
    print("Key is not present in the dictionary")

