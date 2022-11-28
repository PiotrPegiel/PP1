a = input("Podaj nazwę pliku: ")
sum=0
try:
    with open(a) as file:
        for i in file:
            sum+=1
except:
    print("er")
print(f"Number of lines: {sum}")