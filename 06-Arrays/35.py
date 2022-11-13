import random

def rand_elem(arr):
    return arr[random.randint(0,len(arr)-1)]

arr = [random.randint(1,20) for i in range(10)]
print(arr)
print(rand_elem(arr))
print(rand_elem(arr))
print(rand_elem(arr))