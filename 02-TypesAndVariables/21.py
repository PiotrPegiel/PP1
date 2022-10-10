import random


x = random.randint(1,6)
odp = int(input("Take your shot: "))
if(x==odp):
    print(1)
else:
    print(0)