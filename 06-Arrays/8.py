arr = [-1,8,-31,47,-2,-19]
min = arr[0]
max = arr[0]
for i in arr:
    if i < min:
        min = i
    if i > max:
        max = i
print(f'max = {max}. min = {min}')