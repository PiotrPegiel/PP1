try:
    with open("8.txt") as file:
        with open("17.txt","w") as file2:
            for i in file:
                file2.write(i)
except:
    print("er")

try:
    with open("8.txt") as file:
        with open("17.txt") as file2:
            if file.read() == file2.read():
                print(True)
except:
    print("er")