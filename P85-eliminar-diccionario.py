import os; os.system('cls')
''
Municipios={'Apozol':1863,'Calera':1868, 
            'Fresnillo': 1554,'Guadalupe':1821, 
            'Jalpa':1824,'Jerez':1824, 
            'Loreto':1931,'Mazapil':1824,'Momax':1857
            }

print('Diccionario de municipios:')
print(Municipios)

del Municipios['Apozol']
print('Diccionario después de eliminar Apozol:')
print(Municipios)

Municipios.pop('Fresnillo')
print('Diccionario despues de eliminar Fresnillo usando pop: ')
print(Municipios)

Municipios.popitem()
print('Diccionario después de eliminar Momax usando popitem:')
print(Municipios)

Municipios.clear()

print('Diccionario despues de usar clear:')
print(Municipios)