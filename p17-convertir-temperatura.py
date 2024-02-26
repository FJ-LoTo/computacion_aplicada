#Convertir temperatura de celsius a farenheit y viceversa

import os; os.system('cls')

print('Conviertiendo de farenheir a celsius y viceversa\n')
opcion = str.upper(input('[ C ] elsius\n [ F ] arenheit\n elije '))

if opcion == 'C':
    print('\n Conviertiendo a grados celsius')
    temp = float(input('Grados celsius'))
    res = (temp - 32)*5/9
    print(f'{temp} grados Farenheit equivale a {res:.2f} grados celsius')

else:
    print('\n Conviertiendo a grados farenheit')
    temp = float(input('Grados farenheit'))
    res = (temp*5/9) + 32
    print(f'{temp} grados Celsius equivale a {res:.2f} grados Farenheit')

print('Proceso terminado')