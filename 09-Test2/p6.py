def f(n,s):
    import json
    course=[]
    av=[]
    with open("data.json") as fil:
        data = json.load(fil)
    for i in data:
        if i["name"]==n and i["surname"]==s:
            for j in i["studies"]["courses"]:
                course.append(j["name"])
                av.append(sum(j["grades"])/len(j["grades"]))
            return course[av.index(max(av))]