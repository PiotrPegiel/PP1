import random

arr = [random.randint(1,100) for i in range(20)]

even = 0
odd = 0
i = 0
while i!=len(arr):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1
    i+=1
print(f'odd = {odd}, even = {even}')