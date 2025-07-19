# Q9. Write a program to reverse a given number and print.

num = int(input("Enter a number: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10
print("Reverse of the number is: ", rev)
