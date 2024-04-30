import os;
def cuadro(r,c,car):
    print(f'tucuadro teiene {r}x{c} dimensiones y es de {car}')
    for i in range(1,r+1):
        for j in range(1,c+1):
            print(car, end= ' ')
        print('\r')

while True:
    os.system('cls')
    #cuadro(2,4,'s')
    r = int(input('renglones?'))
    c = int(input('columnas?'))
    car = input('caracter?')
    cuadro(r,c,car)
    res = input('deseas otra tabla? (S/N)').upper()
    if res == 'N':
        break