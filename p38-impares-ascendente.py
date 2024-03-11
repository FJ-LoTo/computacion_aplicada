#impares de 1 hasta n 

import os; os.system('cls')

while(True):
    n = int(input('hasta donde? '))
    i = 1
    c=1
    while c<=n:
        if c % 2 == 1:
            print(f'\n {c} \n')
            c=c+1
        else:
            c=c+1

    res= input('deseas continuar(S/N)')
    if res.upper()=='N': break

print('\n proceso terminado')