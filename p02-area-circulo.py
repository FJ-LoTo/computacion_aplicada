#Calcular el area de un circulo

import math #Se importa la libreria

print('Calculando al area de un circulo: \n')

radio = float(input('Dame el area del circulo: '))

area = math.pi * math.pow(radio,2)

print(f'El area el circulo de radio {radio} tiene area de {area:.2f}')