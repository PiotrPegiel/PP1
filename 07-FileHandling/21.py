import random
with open("21.txt","w") as file:
    for i in range(10):
        file.write(str(i+1)+","+str((i+1)**2)+","+str((i+1)**3)+"\n")