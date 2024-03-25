#ciudades

import os; os.system('cls')

print('escribe los nombres de las ciudades con letra \n')

ciudades = []
vocal = ['a','e','i','o','u']
ciudades_cons = []

while True:
    nom = input('ciudad: ')
    if nom == '$':
        break
    ciudades.append(nom)

#    if ciudades.startswith(vocal):
 #       ciudades_cons.append()

ciud_orden = sorted(ciudades)

print(f'lista: {ciudades} | {len(ciudades)}\nEn orden descendente {ciud_orden}\n')