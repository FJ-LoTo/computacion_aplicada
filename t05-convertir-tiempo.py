#Convertir horas en dias, minutos y segundos

import os; os.system('cls')

print('Convertiendo horas en dias, minutos y segundos')

def convertir_horas(horas):
    dias = horas // 24
    horas = horas % 24
    minutos = (horas * 60) % 60
    segundos = (minutos * 60) % 60
    return dias, horas, minutos, segundos

horas = float(input("Introduce las horas: "))
dias, horas, minutos, segundos = convertir_horas(horas)
print(f"{dias:.2f} días, {horas:.2f} horas, {minutos:.2f} minutos y {segundos:.2f} segundos")