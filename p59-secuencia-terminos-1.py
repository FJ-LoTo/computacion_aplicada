#calculando los terminos armonicos

import os; os.system('cls')

print('imprimiendo la secuencia de terminos armonicos ')

n = int(input('cuantos terminos? '))
s=0

for i in range(1,n+1):
    print(f'1/{i}!=', end=' ')
    f = 1
    for j in range(1,i+1):
        f=f*j
    f=1/f
    s=s+f
    print(f'{f}')
print(f'\n la suma es: {s}')