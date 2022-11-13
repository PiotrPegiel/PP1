arr = [[True,False],[True,True],[False,False]]
print(arr)

for i, row in enumerate(arr):
    for j, item in enumerate(row):
        if item == True:
            arr[i][j]=False
        else:
            arr[i][j]=True
print(arr)