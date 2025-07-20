# Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or else handle the exception and print an error message.
def file_content():
    try:
        file_name = input("Enter the file name: ")
        with open(file_name, 'r') as file:
            content = file.read()
            print(content.title())
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
print(file_content())