import random

arr = [random.randint(1,100) for i in range(20)]
print(arr)
even = []
odd = []

for i in arr:
    if i%2==0:
        even.append(i)
        arr.remove(i)
for i in arr:
    if i%2!=0:
        odd.append(i)
        arr.remove(i)
print(even)
print(odd)