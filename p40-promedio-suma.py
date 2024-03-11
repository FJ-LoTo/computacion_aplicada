#promedio suma

import os; os.system('cls')
suma = 0
cantidad = 0
num = 0

while(True):
    n = int(input('Deseas introducir un numero entero? si[1] no[0] '))
    if n == 1:
        num = int(input('introduce el numero '))
        suma = suma + num
        cantidad = cantidad + 1
    else:
        break

    res= input('deseas continuar(S/N) ')
    if res.upper()=='N': break
promedio = suma/cantidad
print(f'\nla suma es {suma} e introdujiste {cantidad} numeros con promedio {promedio:.2f}')
print('\n proceso terminado')