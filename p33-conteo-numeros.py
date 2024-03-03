#imprime numeros del 1 al 200 hasta alcanzar la suma de 100

import os; os.system('cls')

cuenta = suma = 0
cp=cn=cz=0

print('contro de numeros : \n')

while(True):
    num = int(input('numero? '))
    if num!=999:
        cuenta = cuenta +1
        suma = suma+num
        if num > 0 :cp += 1
        elif num <0 : cn += 1
        else : cz += 1
    else:
        break

print(f'\n se introdujeron {cuenta} numeros')
print(f' la suma es {suma}')
print(f' positivos {cp}, negativos {cn}, ceros {cz}')