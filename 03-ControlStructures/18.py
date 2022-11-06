temp = input("Podaj ilość pieniędzy: ")
amount=int(temp)
a = amount//5
amount%=5
b = amount//2
amount%=2
print(f'Hajs {temp} w metalu:\n5zł - {a}\n2zł - {b}\n1zł - {amount}')