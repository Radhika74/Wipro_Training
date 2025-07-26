'''Extract all the text portions between the tags from the following HTML page:
https://raw.githubusercontent.com/selva86/datasets/master/sample.html
Code to retrieve the HTML page is given below:

import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
r.text # html text is contained here

desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph!', 'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']
'''

import requests
import re

r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
html = r.text

texts = re.findall(r'>([^<>]+)<', html)
clean_version = [text.strip() for text in texts if text.strip()]
print(clean_version)
