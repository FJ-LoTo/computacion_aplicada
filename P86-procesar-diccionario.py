import os; os.system("cls")

nombres = ['Juan','Pedro','Manue','Elias','Maria','Felipe','Julia','Roberto']
sueldos = [4550.22,8456.88,1235.12,9998.00,12345.50,29456.55,12234.00,2000.00]

diccionario_sueldos = dict(zip(nombres, sueldos))

print('-'*115)
print('\nDiccionario de sueldos')
print(diccionario_sueldos)

print('\nIterar usando llaves')
for nombre in diccionario_sueldos.keys():
    print(nombre)

print('\nIterar usando valores')
for sueldo in diccionario_sueldos.values():
    print(sueldo)

print('\nIterar usando la llave y el valor con base en la llave')
for nombre in diccionario_sueldos.keys():
    print(nombre,':', diccionario_sueldos[nombre])

print('\nIterar usando el par llave/valor')
for nombre, sueldo in diccionario_sueldos.items():
    print(nombre,':', sueldo)

suma_sueldos = sum(diccionario_sueldos.values())
print('\nSuma de los sueldos', suma_sueldos)

promedio_sueldos = suma_sueldos / len(diccionario_sueldos)
print('Promedio de los sueldos', promedio_sueldos)