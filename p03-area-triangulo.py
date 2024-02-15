#Calcular el area de un triangulo

print('Calculando al area de un triangulo: \n')
print('Dame la base y la altura separados por un Enter: \n')

base, altura = int(input(), int(input()))

area = (base*altura)/2

print(f('El area del triangulo de base {base} y altura {altura} tiene area de {area:.2f}'))