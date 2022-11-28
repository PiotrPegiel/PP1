def convert(m):
    arr = [0 for i in range((len(m)*len(m[0])))]
    temp = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            arr[temp]= m[i][j]
            temp+=1
    return arr
#a
m = [[2,3],[1,5]]
arr = convert(m)
for i in arr:
    print(i,end=",")
print()
#b
m = [[5, 0, 3, 7, 5],[9, 0, 9, 1, 2]]
arr = convert(m)
for i in arr:
    print(i,end=",")
print()
m = [[2,1],[3,5],[7,4],[2,6]]
arr = convert(m)
for i in arr:
    print(i,end=",")