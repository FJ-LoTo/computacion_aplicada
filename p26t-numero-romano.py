#numeros romanos del 1 al 10

import os; os.system('cls')

n1 = int(input('Dame un numero del 1 al 10 para decritelo en romano: '))

print('como se escribe en romano? \n')

if n1==1:
        print(f'l')
elif n1==2:
        print(f'll')
elif n1==3:
        print(f'lll')
elif n1==4:
        print(f'lV')
elif n1==5:
        print(f'V')
elif n1==6:
        print(f'Vl')
elif n1==7:
        print(f'Vll')
elif n1==8:
        print(f'Vlll')
elif n1==9:
        print(f'lX')
elif n1==10:
        print(f'X')
else:
        print(f'{n1} es invalido')
    