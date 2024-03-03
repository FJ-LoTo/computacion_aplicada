#dias de la semana

import os; os.system('cls')

n1 = int(input('Dame un numero de dia de la semana: '))

print('cual dia es? \n')

if n1==1:
        print(f'{n1} es lunes')
elif n1==2:
        print(f'{n1} es martes')
elif n1==3:
        print(f'{n1} es miercoles')
elif n1==4:
        print(f'{n1} es jueves')
elif n1==5:
        print(f'{n1} es viernes')
elif n1==6:
        print(f'{n1} es sabado')
elif n1==7:
        print(f'{n1} es domingo')
else:
        print(f'{n1} es dia invalido')