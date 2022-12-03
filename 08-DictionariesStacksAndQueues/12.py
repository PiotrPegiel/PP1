import json

book = {
    "name":"coolbook",
    "author":"you",
    "year":2077,
    "rating":11,
    "comment":None
}
with open("12.json","w") as f:
    json.dump(book,f,indent=5)