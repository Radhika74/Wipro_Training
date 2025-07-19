# Q5. Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.

for i in range(23,58):
    if i%2==0:
        print(i, end="\t")