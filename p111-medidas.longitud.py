import os

def convertirin(pulgadas):
    centimetros= pulgadas*2.45
    return centimetros

def convertirft(metros):
    pies=metros*3.281
    return pies

os.system('cls')

print('COnversión de longitudes')
print('convertirin pasa de centimetros a pilgadas')
print('convertitft convierte de pies a metros')
resp = int('cual queres usar (1 o2)? ')
medida=('dame la medida: ')
if resp == 1:
    resul=convertirin(medida)
    print(resul)
else:
    resul=convertirft(medida)
    print(resul)