def f(ag,cour,grad):
    import json
    import math
    count = 0
    with open("test.json","r",encoding="utf-8") as f:
        data = json.load(f)
    for i in data:
        for j in i["studies"]["courses"]:
            if j["name"]==cour:
                if sum(j["grades"])/len(j["grades"])>=grad and i["age"]>=ag:
                    count+=1
    return count

#print(f(21,"statistics",4))