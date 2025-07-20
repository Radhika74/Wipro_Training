# Write a program to read first n lines from a txt file. Get n as user input.
def read_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(n):
            print(lines[i])

file_path = 'sample.txt'
n = int(input("Enter the number of lines to read: "))
read_lines(file_path, n)