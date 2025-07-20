# Write a program to read the entire content from a txt file and display it to the user.
file_path = 'sample.txt'

def read_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File Content:\n")
            print(content)
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except IOError:
        print("Error while reading file content")

if __name__ == "__main__":
    file_path = 'sample.txt'
    read_file_content(file_path)
