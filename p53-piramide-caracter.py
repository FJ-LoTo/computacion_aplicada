#imprime una piramide de caracteres

import os; os.system('cls')

print('imprimiendo una piramide del caracter deseado:\n')
n=int(input('cuantos renglones deseas? '))
car=input('caracter? ')

for i in range(1,n+1):
    for j in range(1,i+1):
        print(car, end=' ')
    print('\r')