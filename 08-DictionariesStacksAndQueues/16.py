import json

with open("example2.json",encoding="utf-8") as f:
    data = json.load(f)

result=[]
for i,row in enumerate(data):
    result.append({})
    for key,value in row.items():
        if key!="Id" and key!="Nazwa_produktu" and key!="Nazwa_producenta":
            continue
        else:
            result[i][key]=value

with open("16.json","w",encoding="utf-8") as f:
    json.dump(result,f,indent=4,ensure_ascii=False)