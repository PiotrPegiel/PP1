try:
    with open("8.txt") as file:
        with open("16.txt","w") as file2:
            file2.write(file.read())
except:
    print("er")

try:
    with open("8.txt") as file:
        with open("16.txt") as file2:
            if file.read() == file2.read():
                print(True)
except:
    print("er")