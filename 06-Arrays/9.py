arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
max = 0
for i in arr:
    if len(i) > len(arr[max]):
        max = arr.index(i)
print(f'longest name = {arr[max]}')