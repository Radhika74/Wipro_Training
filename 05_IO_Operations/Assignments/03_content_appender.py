# Write a program to accept input from user and append it to a txt file.
def append_to_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content + '\n')
            print("Content appended successfully.")
    except IOError:
        print("Error while appending content to file.")


file_path = 'sample.txt'
content = input("Enter content to append: ")
append_to_file(file_path, content)
