from math import modf
import math


wzrost = int(input('Podaj swój wzrost w cm: '))
cale, stopy = math.modf(wzrost/30.48)
cale=round(cale, 2)*12
print(f'Mój wzrost to {wzrost}cm. Dla tych gorszych to {int(stopy)} stóp i {cale} cali')