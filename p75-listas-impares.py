#sumar listas de numeros impares

import os; os.system('cls')

n=int(input('hasta donde quieres que cuente tu lista? '))
l1=[]
suma = s3 = 0

for i in range(n+1):
    if i%2!=0:
        l1.append(i)
        suma += i
        if i%3==0:
            print(f'{i} es divisible entre 3')
            s3 += i

prom = suma/len(l1)

search = int(input('Dame un numero a buscar: '))
if search in l1:
    pos = l1.index(search)
    print(f'esta en la posicion {pos}')
else: 
    print('no se encuentra en la lista')

print(f'lista 1 : {l1} \nla suma{suma} y promedio {prom}\n suma de divisibles entre 3 {s3}')