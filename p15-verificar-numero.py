#verificar si un numero es negativo, positivo o cero

import os; os.system('cls')

print('Verificando si un numero entero es negativo, positivo o cero\n')
numero = int(input('Dame un numero entero:'))

if numero>0:
    print('El numero es positivo')

if numero<0:
    print('El numero es negativo')

if numero==0:
    print('El numero es cero')

print('Proceso terminado')