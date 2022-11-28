j = 1
try:
    with open("8.txt") as file:
        for i in file:
            print(i)
            if j%5==0:
                input("press enter")
            j+=1
except:
    print("er")