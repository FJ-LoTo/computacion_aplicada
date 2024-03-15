import os; os.system('cls')

print('suma y promedio de n numeros introducidos por el usuario')

n = int(input('cuantas calificaciones desea capturar? '))

suma = promedio = 0
for i in range(1,n+1):
    print('calificacion {i} : ', end='')
    x = float(input())
    suma=suma+x

promedio = suma/n

print('la suma de calificaciones es {suma} el promedio es {promedio}')