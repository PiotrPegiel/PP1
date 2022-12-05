def f(n,s):
    import csv
    arr=[]
    with open("data.csv") as fil:
        data = csv.reader(fil, delimiter=",")
        for i in data:
            arr.append(i)
    for i in range(1,len(arr)):
        if arr[i][0]==n and arr[i][1]==s:
            return [arr[i][2],arr[i][13]]