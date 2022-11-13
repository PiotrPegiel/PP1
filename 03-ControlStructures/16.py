a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")
if b>a:
    a, b = b, a
print(f'Liczby ustawione rosnąco: {a}, {b}')