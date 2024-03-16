#tabla de multiplicar que el usuario pida hasta donde la pida

import os

while(True):
    os.system('cls')
    print('tabla de multiplicar con for:\n')
    t=int(input('que tabla deseas? '))
    n=int(input('hasta donde la deseas? '))

    for i in range(1,n+1):
        print(f'{t} x {i} = {t*i}')
                

    res = input('deseas continuar(S/N) ')
    if res.upper()=='N': break
print('\n proceso terminado')