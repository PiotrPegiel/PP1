import math

arr = [2,3,7,5,4]
#print(dir(arr))
#a
print(arr)
#b
print(len(arr))
#c
print(arr[0])
#d
print(arr[1])
#e
print(arr[-1])
#f
print(arr[-2])
#g
print(arr[0]+arr[-1])
#h
print(arr[math.floor(len(arr)/2)])
#i
for i in arr:
    print(i,end=" ")
print()
#j
for i in range(0,math.ceil(len(arr)/2)):
    print(arr[i], end=" ")
print()