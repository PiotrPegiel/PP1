def f(dik,x,y):
    sum=0
    for key,val in dik.items():
        for i in val:
            if i>=x and i<=y:
                sum+=i
    return sum
#print(f({"arr1":[4,5,6], "arr2":[7,5]}, 5, 6))