import os;
def estacion(n):
    if n==1:
        est='primaver'
    elif n==2:
        est='verano'
    elif n==3:
        est='otoño'
    elif n ==4:
        est='invierno'
    else:
        est=''
    return est

os.system('cls')
n = int(input('dame la estacion del año(1-4)'))
est=estacion(n)

if est=='':
    print('error')
else:
    print(f'la estacion {n} es {est}')