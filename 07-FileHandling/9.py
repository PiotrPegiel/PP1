sum=0
try:
    with open("9.txt") as file:
        for i in file:
            sum+=int(i)
except:
    print("er")
print(sum)