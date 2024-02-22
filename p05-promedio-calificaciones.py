#calcular el promedio de 3 calificaciones

import os
os.system("cls")

print('Dame el promedio de tres calificaciones\n')
print('Dame tres calificaciones separadas por espacio, pueden tener decimales\n')

c1, c2, c3 = input().split()
c1, c2, c3 = [float(c1), float(c2), float(c3)]
prom = (c1 + c2 + c3) / 3

print(f'El promedio de: {c1},{c2} y {c3} es {prom:.2f}')