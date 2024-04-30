def suma(n1,n2):
    s = n1+n2
    return s

print('suma de dos numeros constantes: ')
s = suma(100,200)
print('la suma es ',s)
print('la suma es ', suma(200,300))

print('dame dos numeros y te doy su suma')
a,b = int(input()), int(input())
res =suma(a,b)
print(f'la suma de {a} + {b} = {res}')