import random

arr = [random.uniform(1,100) for i in range(20)]
a = float(input("Podaj liczbę: "))

count = 0
for i in arr:
    if i>a:
        count+=1
print(count)