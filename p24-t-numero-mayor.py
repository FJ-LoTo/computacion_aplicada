#verifica si los numeros enteros positivos son consecutivos

import os; os.system('cls')

n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
n3 = int(input('numero 3: '))

print('cual numero es mayor? \n')

if n1>n2 and n1>n3:
        print(f'{n1} es el numero mas grande')
elif n2>n1 and n2>n3:
        print(f'{n2} es el numero mas grande')
else:
        print(f'{n3} es el numero mas grande')