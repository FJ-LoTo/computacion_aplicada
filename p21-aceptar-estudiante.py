#aceptar a un estudiante con base en su edad y calificaciones

import os; os.system('cls')

print('Universidad pal perro incorporados y asociados y lo demas\n')
print('Validacion de inscripcion\n')

nombre = input('dame tu nmbre\n')
edad = input('dame tu edad')

if edad < 18:
    print('solo aceptamos estudiantes mayores de edad')
else:
    print('dame dos calificaciones separadas por enter')
    c1, c2 = int(input()), int(input())
if c1<8 or c2<8:
    print('solo aceptamos calificaciones mayores a 8')
else:
    print(f'{nombre} bienvenido a la uni, tu edad {edad} y {c1}, {c2} calificaciones lo permiten')

print('\n proceso terminado')