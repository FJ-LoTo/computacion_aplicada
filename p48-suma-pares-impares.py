import os

while(True):
    os.system('cls')
    n = int(input('hasta donde deseas los numeros? '))

    s=0
    print('numeros pares y su suma')
    for i in range (2,n+1,2):
            print(1,end=' ')
            s=s+1
    print('la suma es ',s)

    s=0
    print('numeros impares y su suma')
    for i in range (2,n+1,2):
            print(1,end=' ')
            s=s+1
    print('la suma es ',s)

    res = input('deseas continuar(S/N) ')
    if res.upper()=='N': break

print('\n proceso terminado')