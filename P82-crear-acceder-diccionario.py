import os; os.system('cls')

dias = {1:'Lunes', 2:'Martes', 
        3:'Miercoles',4:'Jueves', 
        5:'Viernes', 6:'Sábado', 7:'Domingo'
        }

print('dias de la semana:')
print(dias)
print('-'*95)

primer_elemento = dias[1]
print('Primer elemento:', primer_elemento)

ultimo_elemento = dias[7]
print('Ultimo elemento:', ultimo_elemento)

quinto_elemento = dias.get(5)
print('Quinto elemento:', quinto_elemento)

septimo_elemento = dias.get(7)
print('Septimo elemento:', septimo_elemento)

print('-'*95)
print('Diccionario de dias completo:')
print(dias)