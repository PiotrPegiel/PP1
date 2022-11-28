import re

text = "To be, or not to be, that is the question"
find = re.findall("[aeiou]",text)
print(len(find))