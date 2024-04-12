import os; os.system('cls')

materias = ['fisica','quimica','matematicas','geografia','estadistica']
califs = [10,9,9,7.5,6]

print(f'materias : {materias}, {len(materias)}')
print(f'calificaciones : {califs}, {len(califs)}')

notas = dict(zip(materias,califs))
print(f'las notas {notas}, {len(notas)}')

notas.update({'ingles':10})
notas['programacion'] = 7
print(f'las notas {notas}, {len(notas)}')

notas.pop('fisica')
notas.popitem()
print(f'las notas {notas}, {len(notas)}')

notas['quimica'] = 10
notas.update({'matematicas':10, 'geografia':10})
print(f'las notas {notas}, {len(notas)}')

print('\nlista de materias, suma y promedio')
s=p=0
for m, c in notas.items():
    print(f'{m:<12} - {c:5}')
    s=s+c
p=s/len(notas)

print(f'la suma {s} el promedio {p}')

notas.cls()
print(f'las notas {notas}, {len(notas)}')