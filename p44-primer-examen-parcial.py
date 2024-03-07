#inscripción a un evento académico
import os; os.system('cls')

p1 = 100
p2 = 200
p3 = 500
pp1 = 600
pp2 = 800
pp3 = 900
d1 = 0.2
d2 = 0.1
d3 = 0.05
Vtotal = 0

while(True):
    print('Calculando el total por el cargo de ingreso al evento')
    usuario = int(input('Elige el tipo de usuario: Alumno: $100 [1], Trabajador: $200 [2], Docente: $500 [3] '))
    paquete = int(input('Tipo de paquete: Conferencias: $600 [1], Con eventos sociales: $800 [2], Con kit de acceso: $900 [3] '))
    cantidad = int(input('Cantidad? '))

    if usuario == 1 and paquete == 1:
        subtotal = p1*pp1; total = (1-d1)*subtotal
        print(f'Tu pedido fue: {cantidad}, tipo de usuario: Alumno, Tipo de paquete: Conferencias')
        print(f'Subtotal: ${subtotal} con un descuento {d1*100}% y un total de ${total} ')
    elif usuario == 1 and paquete == 2:
        subtotal = p1*pp2; total = (1-d1)*subtotal
        print(f'Tu pedido fue: {cantidad}, tipo de usuario: Alumno, Tipo de paquete: Con eventos sociales')
        print(f'Subtotal: ${subtotal} con un descuento {d1*100}% y un total de ${total} ')
    elif usuario == 1 and paquete == 3:
        subtotal = p1*pp3; total = (1-d1)*subtotal
        print(f'Tu pedido fue: {cantidad}, tipo de usuario: Alumno, Tipo de paquete: Con kit de acceso')
        print(f'Subtotal: ${subtotal} con un descuento {d1*100}% y un total de ${total} ')
    elif usuario == 2 and paquete == 1:
        subtotal = p2*pp1; total = (1-d2)*subtotal
        print(f'Tu pedido fue: {cantidad}, tipo de usuario: Trabajador, Tipo de paquete: Conferencias')
        print(f'Subtotal: ${subtotal} con un descuento {d2*100}% y un total de ${total} ')
    elif usuario == 2 and paquete == 2:
        subtotal = p2*pp2; total = (1-d2)*subtotal
        print(f'Tu pedido fue: {cantidad}, tipo de usuario: Trabajador, Tipo de paquete: Con eventos sociales')
        print(f'Subtotal: ${subtotal} con un descuento {d2*100}% y un total de ${total} ')
    elif usuario == 2 and paquete == 3:
        subtotal = p2*pp3; total = (1-d2)*subtotal
        print(f'Tu pedido fue: {cantidad}, tipo de usuario: Trabajador, Tipo de paquete: Con kit de acceso')
        print(f'Subtotal: ${subtotal} con un descuento {d2*100}% y un total de ${total} ')
    elif usuario == 3 and paquete == 1:
        subtotal = p3*pp1; total = (1-d3)*subtotal
        print(f'Tu pedido fue: {cantidad}, tipo de usuario: Docente, Tipo de paquete: Conferencias')
        print(f'Subtotal: ${subtotal} con un descuento {d3*100}% y un total de ${total} ')
    elif usuario == 3 and paquete == 2:
        subtotal = p3*pp2; total = (1-d3)*subtotal
        print(f'Tu pedido fue: {cantidad}, tipo de usuario: Docente, Tipo de paquete: Con eventos sociales')
        print(f'Subtotal: ${subtotal} con un descuento {d3*100}% y un total de ${total} ')
    elif usuario == 3 and paquete == 3:
        subtotal = p3*pp3; total = (1-d3)*subtotal
        print(f'Tu pedido fue: {cantidad}, tipo de usuario: Docente, Tipo de paquete: Con kit de acceso')
        print(f'Subtotal: ${subtotal} con un descuento {d3*100}% y un total de ${total} ')

    Vtotal = Vtotal + total

    res = input('deseas continuar(S/N) ')
    if res.upper()=='N': break

print(f'Importe total de la venta = {Vtotal}')
print('\n proceso terminado')
