#procesar calificaciones introducidas por el usuario

import os; os.system('cls')

print('procesando calificaciones \n')
print('capturar n calificaciones en el rango de 0 a 100 (0 para terminar) \n')

nums = []
mp = []
n = suma = prom = 0

while True:
    n = float(input('numero: '))
    if n>0 and n<=100:
        nums.append(n)
        suma += n
    elif n == 0:
        print('x')
        break

prom = suma/(len(nums))
for n in nums:
    if n< prom:
        mp.append(n)

prom = suma/(len(nums))

print(f'\n numeros capturados {len(nums)} : {nums}')
print('\n estadisticas')
print(f'la suma es {suma} y el promedio {prom}, menores al promedio {len(mp)} y son {mp}')
print(f'el maximo es {max(nums)} y el minimo es {min(nums)}')