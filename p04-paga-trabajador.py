#calcular la paga de un trabajador

print('calculando la paga de un trabajador: \n')

print('Dame el nombre del trabajador: ')

nombre = input('Nombre del trabajador: ')
horas = int(input('Dame las horas trabajadas: '))
paga = float(input('Dame la paga por hora: '))
tasa = 0.3

pagabruta = horas*paga
impuesto = pagabruta*tasa
paganeta = pagabruta - impuesto

print('\n Resumen de pagos: \n')
print(('El trabajador {nombre}, trabajo {horas} a una tasa de impuestos de {tasa}%'))
print(f'Pagabruta: {pagabruta}')
print(f'Impuesto: {impuesto}')
print(f'Paganeta: {paganeta}')
