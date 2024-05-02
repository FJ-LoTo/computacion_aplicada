import os; os.system('cls')

paises = {'Argentina': 100, 'Brasil': 200, 
          'Colombia': 300, 'Chile': 400, 
          'Ecuador': 500, 'Bolivia': 600, 'Jamaica': 700
        }

print('Diccionario de países completo ')
print(paises)

#asginando valores
paises['Brasil'] = 250
paises['Chile'] = 450
#usando ña funcion upadte
paises.update({'Bolivia': 650})
paises.update({'Jamaica': 750})

print('diccionario de paises modificado: ')
print(paises)