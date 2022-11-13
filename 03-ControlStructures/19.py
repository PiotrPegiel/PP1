humanage = input("Enter the dog's age in human years: ")
humanage = int(humanage)
dogage=0
for i in range(1,humanage+1):
    if i==1 or i==2:
        dogage+=10.5
    else:
        dogage+=4
print(f"The dog's age in dog's years is {dogage} years")
