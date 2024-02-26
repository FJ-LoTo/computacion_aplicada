#angulo3 = 180 – (angulo1 + angulo2)

import os; os.system('cls')

print('Calculando el tercer angulo de un triangulo\n')

angulo1 = float(input('Dame el primer angulo '))
angulo2 = float(input('Dame el segundo angulo '))

angulo3 = 180-(angulo1+angulo2)
print(f'El tercer angulo es {angulo3:.2f}')