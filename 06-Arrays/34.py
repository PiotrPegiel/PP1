def check(a,b):
    for i in a:
        if i not in b:
            return False
    return True
arr1 = [1,2,3,4,5]
arr2 = [1,3,4]

print(check(arr2,arr1))