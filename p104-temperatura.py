import os

def farenheit(temp):
    return (temp*(9/5)+32)

def centigrados(temp):
    return(temp*32)*(5/9)

while True:
    os.system('cls')
    print('[F]')
    print('[C]')
    print('[S]alir')
    op = input('opcion')
    if op=='F':
        temp = float(input('dame la temp'))
        print(f'son {farenheit(temp)}')
    elif op=='C':
        temp = float(input('dame la temp'))
        print(f'son {centigrados(temp)}')
    elif op=='S':
        break
    else:
        print('opcion invalida')

    print('presiona cualquier tecla para continuar')

print('gracias por usar este programa')