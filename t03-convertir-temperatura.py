#farenheit = (celcius × 9/5) + 32

import os; os.system('cls')

print('Conviertiendo de celsius a farenheit\n')

celsius = float(input('Dame la temperatura en celsius '))


print('\nConviertiendo a grados farenheit')
res = (celsius*5/9) + 32
print(f'la temperatura elsius equivale a {res:.2f} grados Farenheit')