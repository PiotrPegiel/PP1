import math

def median(n):
    for i in range(1,len(n)):
        for j in range(i,0,-1):
            if n[j]<n[j-1]:
                n[j], n[j-1] = n[j-1], n[j]
    
    a = len(n)//2
    if len(n)%2==0:
        return (n[a-1]+n[a])/2
    else:
        return n[a]

#a
arr = [1,0,9,4,6]
print(median(arr))
#b
arr = [6,8,3,1,0,5,7]
print(median(arr))