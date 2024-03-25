import os; os.system('cls')

meses = ['enero','febrero','marzo','mayo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
numdias = [31,28,31,30,31,30,31,31,30,31,30,31]

while True:
    mes = input('dame un mes, entre con letra: ')
    if mes in meses:
        break
print('el mes que elejiste es ', mes)

pos = meses.index(mes)
print(f'tiene {numdias[pos]} dias ')