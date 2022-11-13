def create_2d_arr(x,y):
    arr = [[0 for i in range(x)] for j in range(y)]
    return arr
arr = create_2d_arr(3,5)
print(arr)