#Calcula la paga de un trabajador considerando las horas extra

import os; os.system('cls')

print('Calculando la paga de horas extra de un trabajador\n')

nombre = input('Nombre del trabajador ')
horas = int(input('Horas trabajadas '))
paga = float(input('Paga por hora '))

extra = pagaextra = total = 0

if horas <= 40:
    total = horas + paga
else:
    extra = horas -40
    pagaextra = extra*paga*2
    total = (40*paga)+pagaextra


salida = ('\n El trabajador {nombre} \n'
f'trabajo {horas} horas'
f'horas extra {extra}, paga extra {pagaextra}'
f' total de pago {total}'
)

print(salida)