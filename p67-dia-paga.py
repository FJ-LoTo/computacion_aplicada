#da la paga correspondiente a un dia

import os; os.system('cls')

dias=['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
paga=[100,200,300,400,500,600,700]

while True:
    dia = input('dame un dia de la semana entre con letra: ')
    if dia in dias:
        break
print('el dia que elejiste trabajar es ', dia)
pos = dias.index(dia)
print('la paga que te corresponde es ', paga(pos))