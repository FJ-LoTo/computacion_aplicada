import os; os.system('cls')

ventas = {'Juan':1550,'Jose':2600,'Maria':2220}

print("Diccionario de ventas:")
print(ventas)

ventas['Rocio'] = 2500
ventas['Mateo'] = 1567
ventas.update({'Andrea':9567,'Miguel':1234})

print('\nDiccionario de países despues de agregar elementos adicionales:')
print(ventas)