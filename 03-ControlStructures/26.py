correct = 1234
for i in range(3):
    pin = int(input("Podaj Pin: "))
    if correct == pin:
        break
    print("Błędny kod")
    if i==2:
        print("Zablokowano kartę")