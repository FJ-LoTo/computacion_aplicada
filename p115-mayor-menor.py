import os;

def mayor(lista):
    m=lista[0]
    for n in range (len(lista)):
        if lista[n]>m:
            m=lista[n]
    return m

def menor(lista):
    m=lista[0]
    for n in range (len(lista)):
        if lista[n]<m:
            m=lista[n]
    return m

def leer():
    nums=[]
    while True:
        d = int(input('numero? '))
        if d == -1: break
        nums.append(d)
    return nums

os.system('cls')
nums=leer()
may=mayor(nums)
men=menor(nums)
print(f'los numeros osn {nums}, {len(nums)}')
print('el masyor es ', may)
print('el menor es ', men)