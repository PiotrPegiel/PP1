input = input("Podaj produkt: ")
with open("12.txt","a") as file:
    file.write("\n"+input)