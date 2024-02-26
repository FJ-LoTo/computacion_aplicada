#Dado el año de nacimiento, la suma de sus dígitos individuales es el número de la suerte.

import os; os.system('cls')

print('Obteniendo tu numero de la suerte\n')

print('Dame tu cumpleaños separado por un enter')
n1, n2, n3 = int(input()), int(input()), int(input())

suerte = n1+n2+n3

print(f' tu numero de la suerte es {suerte} GOOD LUCK!!!')