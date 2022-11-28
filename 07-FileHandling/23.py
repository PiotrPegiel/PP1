import re

forecast = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temp = re.findall("\d{2}",forecast)
sum=0
for i in temp:
    sum+=int(i)
print(sum/len(temp))