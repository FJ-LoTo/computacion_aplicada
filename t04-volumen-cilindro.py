#Volumen = PI * (Radio * Radio) * Altura

import os; os.system('cls')
import math

print('Calculando el volumen de un cilindro\n')

radio = float(input('Radio en cm'))
altura = float(input('Altura en cm'))

volumen = math.pi*(radio*radio)*altura
print(f'El volumen del cilindro es {volumen:.2f} cm3')