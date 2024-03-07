#calcula e imprime las tablas ashata n
import os; os.system('cls')

while(True):
    print('imprimiendo la tabla de multiplicar deseada')

    n = int(input('hasta que tabla quieres? '))
    m = int(input('hasta donde quieres la tabla? '))
    t=1
    while t<=n:
        print(f'\n Tabla del {t} \n')
        c=1
        while c <=m:
            print(f'{t} x {c} = {t*c}')
            c+=1

        t+=1

    res= input('deseas continuar(S/N)')
    if res.upper()=='N': break

print('\n proceso terminado')