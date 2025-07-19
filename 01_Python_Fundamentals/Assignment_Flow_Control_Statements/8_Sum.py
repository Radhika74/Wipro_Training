# Q8. Write a program to print the sum of all the digits of a given number.

num = int(input("Enter a number: "))
sum = 0
while num > 0:
    sum += num % 10
    num = num // 10
print("Sum: ", sum)
