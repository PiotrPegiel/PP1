def f(fir,las):
    import re
    with open("test.txt", "r", encoding="utf-8") as f:
        data = f.read()
        data = re.split("\W",data)
        count=0
        for i in data:
            if(re.match(f"^{fir}\w*{las}$",i)):
                count+=1
        return count
print(f("w","d"))