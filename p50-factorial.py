#calculando el factorial de un numero

import os; os.system('cls')

print('imprimiendo el factoria de un numero')

n = int(input('dame un nmero entero '))

f=1

for i in range(1,n+1):
    f = f+i

print(f'\n el factorial es {f}')