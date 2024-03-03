#verifica si los numeros enteros positivos son consecutivos

import os; os.system('cls')

n1 = int(input('numero 1: '))
n2 = int(input('numero 2: '))
n3 = int(input('numero 3: '))

print('numeros consecutivos o no : \n')
valida = n3-n1

if valida == 2:
        print(f'son consecutivos')
else:
        print(f'no son consecutivos')

