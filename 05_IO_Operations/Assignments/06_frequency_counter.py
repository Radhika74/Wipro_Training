# Write a program to count the frequency of a user entered word in a txt file.
def count_frequency(file_path, word):
    with open(file_path, 'r') as file:
        content = file.read()
        words = content.split()
        return words.count(word)

file_path = 'sample.txt'
word = input("Enter a word to count its frequency: ")
print(count_frequency(file_path, word))
