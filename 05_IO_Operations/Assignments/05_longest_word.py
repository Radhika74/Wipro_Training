# Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
def find_longest_word(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
        longest_word = max(words, key=len)
        return longest_word

file_path = 'sample.txt'
print(find_longest_word(file_path))
