a=1
i=0
sum=0
while(1):
    a = int(input("Podaj cyfrę: "))
    if a==0:
        break
    sum+=a
    i+=1
print(f"ilość: {i}, suma: {sum}, średnia: {sum/i}")