import json

student = {
    "name":"Piotr",
    "surname":"Pęgiel",
    "id":True,
    "pesel":55555555555,
    "studies":["it","admin"],
    "grades":[
        {"name":"it",
        "grade":[1,2,3]},
        {"name":"admin",
        "grade":[3,2,1]},
    ]
}

with open("13.json","w",encoding="utf-8") as f:
    json.dump(student,f,indent=4,ensure_ascii=False)