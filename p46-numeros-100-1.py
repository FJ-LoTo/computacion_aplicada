#numeros for

import os; os.system('cls')
x = int(input('desde donde? '))
y = int(input('de cuanto en cuanto? '))

for c in range(x, 0, -y):
    print(c, end = ' ')