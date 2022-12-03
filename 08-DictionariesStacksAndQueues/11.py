import json

with open("example.json",encoding="utf-8") as file:
    data = json.load(file)

for k,v in data.items():
    print(k,":",v)