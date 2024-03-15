#numeros for

import os; os.system('cls')
x = int(input('hasta donde? '))
y = int(input('de cuanto en cuanto? '))

for n in range(0, x+1, y):
    print(n, end = ' ')