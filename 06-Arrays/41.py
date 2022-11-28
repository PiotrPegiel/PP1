import random
arr = [[random.randint(0,9) for i in range(3)] for j in range(5)]
for i in arr:
    print(i)
print()

for i in range(3):
    arr[0][i], arr[-1][i] = arr[-1][i],arr[0][i]

for i in arr:
    print(i)