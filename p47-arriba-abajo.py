#numeros del 1 a n o viceversa segun decia el usuario

import os

while(True):
    os.system('cls')
    print('[1] numeros de 1 a n')
    print('[2] numeros de n a 1')
    print('[3] salir')
    op = int(input('elige '))
    if op == 1: 
        n = int(input('hasta donde? '))
        for c in range (1,n+1):
            print(c,end=' ')
    elif op==2:
        n = int(input('hasta donde? '))
        for c in range (n,0,-1):
            print(c,end=' ')
    elif op==3:
        break
    else:
        print('opcion incorrecta')

    res = input('deseas continuar(S/N) ')
    if res.upper()=='N': break
print('\n proceso terminado')