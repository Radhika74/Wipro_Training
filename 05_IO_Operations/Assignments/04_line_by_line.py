# Write a program to read contents from a txt file line by line and store each line into a list.
def list_file_content(file_path):
    lines = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print("Error reading the file.")
    return lines

file_path = 'sample.txt'  
line_list = list_file_content(file_path)
print("Lines in file as list:")
print(line_list)
