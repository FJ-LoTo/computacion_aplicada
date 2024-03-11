#pares de 100 a n

import os; os.system('cls')
suma = 0

while(True):
    n = int(input('hasta donde? '))
    i = 1
    c=100
    while c<=n:
        if c % 2 == 0:
            print(f'{c} \n')
            c=c+1
            suma = suma + c
        else:
            c=c+1

    res= input('deseas continuar(S/N)')
    if res.upper()=='N': break

print(f'\nla suma es {suma}')
print('\n proceso terminado')