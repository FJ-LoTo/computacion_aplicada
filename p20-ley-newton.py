import os; os.system('cls')

print('Calculando los valores de la segunda ley de Newton\n')
print('[ f ] = m * a')
print('[ m ] = f / a')
print('[ a ] = f / m')

op = input('elige una opcion ').lower()

if op=='f' :
    print('calculando la fuerza')
    m = float(input('dame la masa '))
    a = float(input('dame la aceleracion '))
    f = m * a
    print('la fuerza es ', f)
elif op=='m' :
    print('calculando la masa')
    f = float(input('dame la fuerza '))
    a = float(input('dame la aceleracion '))
    m = f / a
    print('la fuerza es ', m)
elif op== 'a':
    print('calculando la aceleracion')
    f = float(input('dame la fuerza '))
    m = float(input('dame la masa '))
    a = f / m
    print('la fuerza es ', a)
else:
    print('\n opcion incorrecta')

print('\n proceso terminado')