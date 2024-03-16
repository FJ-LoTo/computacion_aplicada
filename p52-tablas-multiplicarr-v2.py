#tabla de multiplicar del 1 al n hasta m

import os; os.system('cls')

print('tabla de multiplicar con for:\n')
n=int(input('hasta que tabla deseas? '))
m=int(input('hasta donde la deseas? '))

for i in range(1,n+1):
    print(f'\ntabla del {i}')
    for j in range(1, m+1):
        print(f'{i} x {j} = {i*j}')
