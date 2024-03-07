#imprimir una tabla de conversion de pedo a dolar usando while

while(True):
    import os; os.system('cls')

    tc = 17.00

    print('tabla de conversion de peso a dolar: \n')
    pi = float(input('valor inicial: '))
    pf = float(input('valor final: '))

    c = pi
    print('Peso\tDolar')
    print('-'*15)
    while c <= pf:
        print(f'{c}\t{c/tc:.2f}')
        c = c+1
    print('-'*15)

    res= input('deseas continuar(S/N)')
    if res.upper()=='N': break

print('\n proceso terminado')