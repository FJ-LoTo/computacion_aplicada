#numero mayor de los ingresados

import os; os.system('cls')
cantidad = 0
numeros = []

while(True):
    siono = int(input('Deseas introducir un numero entero? si[1] no[0] '))
    if siono == 1:
        num = int(input('introduce el numero [0] para salir '))
        numeros.append[num]

    res= input('deseas continuar(S/N) ')
    if res.upper()=='N': break
print(f'el numero mayor es {max(numeros)}')
print('\n proceso terminado')