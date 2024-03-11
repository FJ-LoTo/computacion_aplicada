#imprime numeros introducidos hasta 200

import os; os.system('cls')
suma = 0
cantidad = 0

while(True):
    n = int(input('Deseas introducir un numero entero? si[1] no[0] '))
    if n == 1 and suma <= 200:
        num = int(input('introduce el numero '))
        suma = suma + num
        cantidad = cantidad + 1
        if suma >= 200:
            break
    else:
        break

    res = input('deseas continuar(S/N) ')
    if res.upper()=='N': break

print(f'\nla suma es {suma} e introdujiste {cantidad} numeros ')
print('\n proceso terminado')