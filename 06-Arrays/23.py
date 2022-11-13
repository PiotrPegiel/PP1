import random

def bubblesort(n):
    for i in range(1,len(n)):
        for j in range(i,0,-1):
            if n[j]<n[j-1]:
                n[j], n[j-1] = n[j-1], n[j]
    return n

arr1 = [random.randint(1,100) for i in range(5)]
arr2 = [random.randint(1,100) for i in range(5)]
arr3 = [random.randint(1,100) for i in range(5)]

print(arr1)
print(bubblesort(arr1))
print()
print(arr2)
print(bubblesort(arr2))
print()
print(arr3)
print(bubblesort(arr3))
print()