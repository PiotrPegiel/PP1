#http://api.nbp.pl/
#http://api.nbp.pl/api/exchangerates/rates/c/eur/last/10/?format=json

import json

#sprawia że kod json'a jest czytelny:
with open("17.json", "r") as f:
    data = json.load(f)
with open("17.json", "w") as f:
    json.dump(data,f,indent=4)
#end

print(f"Date                Buying Rate     Selling Rate")
print(f"================================================")
for i,row in enumerate(data["rates"]):
    for key,value in row.items():
        if key!="no":
            if key!="ask":
                print(value,end="             ")
            else:
                print(value)