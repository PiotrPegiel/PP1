try:
    with open("filename.txt") as file:
        for i in file:
            print(i, end="")
except:
    print("er")