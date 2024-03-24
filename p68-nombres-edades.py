#captura una lista de edadesy nombres

import os; os.system('cls')

nombres = []
edades = []

print('introduce los nombres y edades de n estudiantes: * para terminar')

while True:
    nombre = input('nombre: ')
    if nombre == '*':
        break
    else: 
        nombres.append(nombre)
        edad= int(input('edad: '))
        edades.append(edad)

print(f'nombres: {nombres} y edades {edades}')

print('\n alumnos mayores de edad:')
for i in range(len(nombres)):
    if edades[i] >=0:
        print(f'nombre: {nombres[i]}, edades: {edades[i]}')

may =  max(edades)
pos = edades.index(may)
print(f'el alumnos de mayor edad es  {nombre(pos)} y tiene {edades(pos)} años')