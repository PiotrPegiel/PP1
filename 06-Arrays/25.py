def occurs(a, arr):
    if a in arr:
        return True
    else:
        return False

arr = [15, 38, 7, 23, 14]
a = int(input("Podaj cyfrę: "))
print(occurs(a,arr))