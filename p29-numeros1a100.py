#imprime numeros de 1 a n de 1 en 1

import os; os.system('cls')

n = int(input('hasta donde?'))
i = int(input('incremento?'))

c=1
while c<=n:
    print(c,end='')
    c=c+1