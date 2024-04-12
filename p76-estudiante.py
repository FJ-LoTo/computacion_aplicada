import os; os.system('cls')

estudiante = {'nombre' : 'juan perez', 'edad' : 45, 'email' : 'email@msg.com', 'carrera' : 'sistemas'}
estudiante2 = {'nombre' : 'maria lopez', 'edad' : 22, 'email' : 'm,aria@msg.com', 'carrera' : 'leyes'}

print(f'elestudiante \n {estudiante}, {len(estudiante)}')

print('\n las llaves:')
for k in estudiante.keys():
    print(k)

print('\n los valores')
for v in estudiante.values():
    print(v)

estudiante.update({'calificacion':9.5})
estudiante['email'] = 'gmail@mgs.com'

print('\nEL diccionario modificado, llave y valor')
for k, v in estudiante.items():
    print(f'{k:<12} - {v:>15}')

print(f'el estudiante: \n {estudiante2}, {len(estudiante2)}')