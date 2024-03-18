#imprime numeros iguales en renglon en piramide

import os; os.system('cls')

n = int(input('Dame un numero '))
s=0
for c in range (1,n+1):
    s=s+1
    for i in range(1,c+1):
        print(s,end=' ')
    print('')