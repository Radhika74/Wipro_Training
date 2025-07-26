'''Given below list of words, identify the words that begin and end with the same character.
civic
trust
widows
maximum
museums
aa
as '''

import re

words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
pattern = re.compile(r'^(.).*\1$')

for w in words:
    if pattern.match(w):
        print(w)
