#imprime cuenta de numeros en piramide

import os; os.system('cls')

n = int(input('Dame un numero '))
for c in range (1,n+1):
    for i in range(1,c+1):
        print(i,end=' ')
    print('')