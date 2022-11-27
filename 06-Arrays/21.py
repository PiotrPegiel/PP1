def compare(a,b):
    if a==b:
        return True
    else:
        return False

#a
arr1 = ["water","book","sky"]
arr2 = ["water","book","sky"]
print(arr1)
print(arr2)
print(compare(arr1,arr2))

#b
arr1 = [True,False]
arr2 = [True,False,True]
print(arr1)
print(arr2)
print(compare(arr1,arr2))

#c
arr1 = [5,3,1]
arr2 = [5,3,1]
print(arr1)
print(arr2)
print(compare(arr1,arr2))

#d
arr1 = [3,2,1]
arr2 = [3,2]
print(arr1)
print(arr2)
print(compare(arr1,arr2))