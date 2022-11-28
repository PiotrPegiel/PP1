temp = False
with open("22.csv") as file:
    for i in file:
        if temp == True:
            arr = i.split(",")
            if int(arr[2])<30:
                print(f"{arr[0]} {arr[1]} {arr[-1]}")
        else:
            temp = True