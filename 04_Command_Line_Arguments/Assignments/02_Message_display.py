# Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.
import sys
import os
if len(sys.argv) < 2:
    print("Usage: python welcome_message.py <welcome message>")
else:
    file_name = os.path.basename(__file__)
    welcome_message = ' '.join(sys.argv[1:])
    print(f"File Name     : {file_name}")
    print(f"Welcome Message: {welcome_message}")
