arr = [[-38, 19],[5,40],[-7,11],[29,16]]
minv = 0
maxv = 0
for i in range(4):
    for j in range(2):
        if arr[i][j]>maxv:
            maxv = arr[i][j]
            maxx = j
            maxy = i
        if arr[i][j]<minv:
            minv = arr[i][j]
            minx = j
            miny = i
print(f'najmniejsza wartość to {minv}, na pozycjach {minx} {miny}')
print(f'największa wartość to {maxv}, na pozycjach {maxx} {maxy}')