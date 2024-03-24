#procesar calificaciones introducidas por el usuario

import os; os.system('cls')

print('procesando calificaciones \n')
print('capturar n calificaciones en el rango de 1 a 10 (99 para terminar) \n')

nums = []
mp = []
n = suma = prom = 0

while n!=99:
    n = float(input('numero: '))
    if n>=0 and n<=10:
        nums.append(n)
        suma += n
    else:
        print('x')

prom = suma/len(nums)
for n in nums:
    if n>= prom:
        mp.append(n)

print(f'\n numeros capturados {len(nums)} : {nums}')
print('\n estadisticas')
print(f'la suma es {suma} y el promedio {prom}, mayores al promedio {len(mp)} y son {mp}')
print(f'el maximo es {max(nums)} y el minimo es {min(nums)}')