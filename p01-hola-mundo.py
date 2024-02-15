#leer datos y enviar un saludo

print('Leyendo datos y enviando un saludo; \n')

nombre = input('Dame tu nombre: ')
edad = int(input('Dame tu edad: '))
peso = float(input('Dame tu peso: '))

print(f'tu nombre es {nombre} tu edad es {edad} tu peso es {peso}')

alerta = peso > 65

print (type(nombre))
print (type(edad))
print (type(peso))
print (type(alerta))