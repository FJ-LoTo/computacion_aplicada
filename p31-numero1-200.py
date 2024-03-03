#imprime numeros del 1 al 200 en incrementos de 10

import os; os.system('cls')

m = int(input('multiplos?'))

c=0
while c<=200:
    c+=1
    if c % m != 0:
        continue
    print(c,end=' ')