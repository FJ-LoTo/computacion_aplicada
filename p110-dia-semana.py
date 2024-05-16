import os;

def dias(numero):
    if numero==1:
        dias='lundi'
    elif numero==2:
        dias='mardi'
    elif numero==3:
        dias='mercredi'
    elif numero==4:
        dias='jeudi'
    elif numero==5:
        dias='vendredi'
    elif numero==6:
        dias='samedi'
    elif numero==7:
        dias='dimanche'
    return dias

os.system('cls')
numero = int('dame un numero de dia? ')
diasemana=dias(numero)
print('el dia es ', diasemana)