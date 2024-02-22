#Dividir un numero de 3 cifras en sus cifras individuales

import os; os.system('cls')
import math

print('Dividir en unidades, decenas, centenas y millares un numero entero')

numero = int(input('Dame un número de 4 cifras:'))

unidades = numero % 10
numero //= 10
decenas = numero % 10
numero //= 10
centenas = numero % 10
numero //= 10
millares = numero % 10
numero //= 10

print(f'millares: {millares}, centenas: {centenas}, decenas: {decenas}, unidades: {unidades}')