#multiplicar listas introducidas por el usuario

import os; os.system('cls')

lista1=[]
lista2=[]
lista3=[]

c = 5

print(f'\n dame los {c} numeros de la lista 1:')
for i in range(c):
    n=int(input(f'lista1[{i}] = '))
    lista1.append(n)
print(f'lista 1 : {lista1} , {len(lista1)}')

print(f'\n dame los {c} numeros de la lista 2:')
for i in range(c):
    n=int(input(f'lista2[{i}] = '))
    lista2.append(n)
print(f'lista 2 : {lista2} , {len(lista2)}')

print('\n calculando la multiplicacion de las listas')
for i in range(c):
    lista3.append(lista1[i]*lista2[i])

print(f'lista 3: {lista3} , {len(lista3)}')