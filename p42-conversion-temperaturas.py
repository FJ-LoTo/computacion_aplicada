#conversion de temperatura

import os; os.system('cls')

while(True):
    tc = 17.00
    pi = float(input('valor inicial: '))
    pf = float(input('valor final: '))

    c = pi
    print('Celsius\tFarenheit')
    print('-'*15)
    while c <= pf:
        print(f'{c}\t{c*1.8 + 32:.2f}')
        c = c+1
    print('-'*15)

    res = input('deseas continuar(S/N) ')
    if res.upper()=='N': break

print('\n proceso terminado')