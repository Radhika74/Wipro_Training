# Make a dictionary of the 26 English alphabets mapping each with the corresponding integer.
letters = 'abcdefghijklmnopqrstuvwxyz'
get_pair = lambda x: (x, ord(x) - 96)
pairs = map(get_pair, letters)
alphabet_dictionary = dict(pairs)
print(alphabet_dictionary)
