#aceptar a un estudiante con base en su edad, calificaciones y genero

import os; os.system('cls')


print('Universidad Kitty Kat SA de CV\n')
print('Validacion de inscripcion\n')

nombre = input('dame tu nmbre\n')
edad = int(input('dame tu edad\n'))
genero = int(input('dime tu genero (M=1) (H=2)\n'))
print('dame tres calificaciones separadas por espacio')
c1, c2, c3 = input().split()
c1, c2, c3 = int(c1), int(c2), int(c3)
promedio = (c1+c2+c3)/3


if genero == 2:
    print(f'{nombre}, {edad} años {c1}, {c2}, {c3} solo aceptamos mujeres')
elif edad < 21:
    print(f'{nombre}, {edad} años {c1}, {c2}, {c3} lo permiten pero solo aceptamos mayores de 21 años')
elif 8 >= promedio <=9.5:
    print(f'{nombre}, {edad} años {c1}, {c2}, {c3} tu promedio no permite')
else:
    print(f'{nombre} bienvenida a la uni, tu edad {edad} y {c1}, {c2}, {c3} calificaciones lo permiten')

print('\n proceso terminado')