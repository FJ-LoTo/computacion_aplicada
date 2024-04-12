import os; os.system('cls')

datos = {}

print(f'datos {datos}, {len(datos)}')

print('introduce nombre y edades (nombre vacio para terminar):')
while True:
    nombre = input('dame el nombre: ')
    if nombre!='':
        datos[nombre] = int(input('dame la edad: '))
        #datos['peso'] = float(input('peso: '))
    else:
        break

print(f'datos {datos}, {len(datos)}')

print('\nlistado de nombres, suma y promedio')
s=p=0
for n, e in datos.items():
    print(f'{n:<20} - {e:3}')
    s=s+e
p=s/len(datos)

print(f'la suma es {s} y el promedio es {p }')