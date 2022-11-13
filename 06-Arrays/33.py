import random

arr = [random.randint(1,999) for i in range(8)]
print(arr)
res = ""

for i in arr:
    res+="| "
    match len(str(i)):
        case 3:
            res+=str(i)
        case 2:
            res+=" "
            res+=str(i)
        case 1:
            res+="  "
            res+=str(i)
res+="|"

print("-"*len(res))
print(res)
print("-"*len(res))