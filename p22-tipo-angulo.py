#muestra el tipo de angulo

import os; os.system('cls')

print('mostrando el tipo de angulo con base en los grados\n')
angulo = int(input('dame el angulo '))

if angulo < 90:
    print('agudo')
elif angulo == 90:
    print('recto')
elif angulo > 90:
    print('obtuso')
elif angulo == 180:
    print('llano')
elif angulo > 180 and angulo < 360:
    print('concavo')
else:
    print('angulo fuera de rango')

print('\n proceso terminado')