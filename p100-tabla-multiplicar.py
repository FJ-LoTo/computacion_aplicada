import os;
def tabla(t,n):
    print(f'imprimiendo la tabla del {t} hasta el {n}')
    for i in range(1,n+1):
        print(f'{t} x {i} = {t*i}')

#tabla(6,10)
#tabla(3,4)
while True:
    os.system('cls')
    t=int(input('que tabla? '))
    n = int(input('hasta donde? '))
    tabla(t,n)
    res = input('deseasotra tabla? (S/N)').upper()
    if res=='N':
        break