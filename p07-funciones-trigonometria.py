#uso de las funciones trigonometricas en el modulo math

import os; os.system('cls')
import math

print('Calcuolo de funciones trigonométricas\n')
angulo = float(input('Dame un angulo (radianes):'))

seno = math.sin(angulo)
coseno = math.cos(angulo)
tangente = math.tan(angulo)

grados = math.degrees(angulo)

salida = ('\nResumen de las funciones trigonométricas\n' f'El seno: {seno}\n' f'El coseno: {coseno}\n' f'La tangente: {tangente}\n' f'El angulo {angulo} en radianes equivale a {grados}\n')

print(salida)