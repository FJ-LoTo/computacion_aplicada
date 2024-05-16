import os;

def leer():
    nums=[]
    while True:
        d = int(input('numero? '))
        if d == -1: break
        nums.append(d)
    return nums

def promedio(lista):
    s=0
    for n in lista:
        s+=n
    return s/len(lista)

def mayorprom(lista,prom):
    mp=[]
    for n in lista:
        if n>prom:
            mp.append(n)
    return mp

os.system('cls')
nums=leer()
prom=promedio(nums)
mp=mayorprom(nums,prom)
print(f'los numeros osn {nums}, {len(nums)}')
print('el promedio es ', prom)
print(f'mayores al pro,medio {mp} , {len(mp)}')