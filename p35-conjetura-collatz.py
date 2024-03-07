#calcula e imprime la conjetura de collatz
import os; os.system('cls')

while(True):
    print('imprimiendo los numeros de la cpnjetura de collatz')

    num = int(input('dame un numero entero positivo: '))

    while num != 1:
        print(num, end = ' ')
        if num % 2 == 0:
            num /= 2
        else:
            num = num*3 + 1

    print(num)

    res= input('deseas continuar(S/N)')
    if res.upper()=='N': break

print('\n proceso terminado')