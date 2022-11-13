arr = [5,1,9,6,1]

a = max(arr)
b = arr[0]
for i in arr:
    if i>b and i!=a:
        b=i
print(b)