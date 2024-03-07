#calcula e imprime las tablas ashata n
import os; os.system('cls')

while(True):
    print('imprimiendo la tabla de multiplicar deseada')

    t = int(input('que tabla quieres? '))
    n = int(input('hasta donde quieres la tabla? '))
    c=1
    while c<=n:
        print(f'{t} x {c} = {t*c}')
        c += 1

    res= input('deseas continuar(S/N)')
    if res.upper()=='N': break

print('\n proceso terminado')