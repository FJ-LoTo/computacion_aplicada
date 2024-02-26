#verificar si la suma de dos numeros es igual a un tercero

import os; os.system('cls')

print('Verificando si la suma de dos numeros es igual a un tercero\n')
print('Dame tres numeros enteros separados por un enter')
n1, n2, n3 = int(input()), int(input()), int(input())

if n1+n2==n3:
    print('Son iguales')
else:
    print('Son diferentes')

print('Proceso terminado')