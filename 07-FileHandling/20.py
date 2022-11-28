import random
with open("20.txt","w") as file:
    for i in range(50):
        file.write(str(random.randint(100,999))+"\n")