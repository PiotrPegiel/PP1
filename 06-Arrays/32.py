arr = [5,4,3,2,6,5]
print(arr)

a = ""
for i in arr:
    a+=str(i)
    a+=","
a = a[:-1]
print(a)