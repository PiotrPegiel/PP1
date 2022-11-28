with open("18#1.txt") as file:
    with open("18#2.txt") as file2:
        with open("18#3.txt","w") as file3:
            file3.write(file.read()+"\n"+file2.read())