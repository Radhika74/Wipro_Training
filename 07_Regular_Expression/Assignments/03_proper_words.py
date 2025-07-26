# Split the following irregular sentence into proper words sentence = """A, very very; irregular_sentence""" ## expected output : A very very irregular sentence

import re

sentence = "A, very very; irregular_sentence"
words = re.split(r'[;,_\s]+', sentence)
result = ' '.join(words)
print(result)