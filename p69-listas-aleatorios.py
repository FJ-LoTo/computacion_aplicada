#sumar listas de numeros aleatorios

import random
import os; os.system('cls')

n=10
l1=[]
l2=[]
l3=[]

for i in range(n):
    l1.append(random.randint(1,10))
    l2.append(random.randint(1,10))

print(f'lista 1 : {l1}\nlista2: {l2}')

for i in range(n):
    l1[i] = l1[i]**2
    l2[i] = l2[i]**2
    l3.append(l1[i]+l2[i])

print(f'\n lista 1: {l1}\nlista2: {l2}\nlista3: {l3}')