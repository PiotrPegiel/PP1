import re

with open("8.txt") as file:
    arr = re.findall("\w{6,}",file.read())
print(arr)