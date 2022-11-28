import random
arr = [[random.randint(0,9) for i in range(3)] for j in range(5)]
for i in arr:
    print(i)
print()

for i in range(5):
    arr[i][0], arr[i][-1] = arr[i][-1],arr[i][0]

for i in arr:
    print(i)