#calculando el factorial de un numero

import os; os.system('cls')

print('imprimiendo el factoria de n numeros ')

n = int(input('de cuantos numeros deseas el factorial '))

for i in range(1,n+1):
    print(f'{i}!=', end=' ')
    f = 1
    for j in range(1,i+1):
        f = f*j
    print(f'{f}')

print(f'\n el factorial es {f}')