import re

with open("27.txt") as file:
    file.readline()
    text = file.readline()

text = re.sub("\D*","",text,1)
text = re.split("\, ",text)
sum = 0
for i in text:
   sum+=float(i)
print(round(sum/len(text),2))