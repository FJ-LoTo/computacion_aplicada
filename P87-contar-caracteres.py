import os; os.system('cls')

cadena = input('Ingrese una cadena s´il vous plais')

frec_caracteres = {}

for caracter in cadena:
    if caracter in frec_caracteres:
        frec_caracteres[caracter]+=1
    else:
        frec_caracteres[caracter]=1

print('Cantidad de apariciones de cada carácter')
print(frec_caracteres)