import os;

def pi(lista):
    lp = []
    li=[]
    for n in lista:
        if n%2==0:
            lp.append(n)
        else:
            li.append(n)
    return lp,li

def nums(ini,fin):
    list=[]
    for i in range(ini,fin):
        list.append(i)
    return list

os.system('cls')

ini = int('desde donde? ?')
fin = int('hasta donde? ')
lista = nums(ini,fin)
print('la lista',lista)
lp,li = pi(lista)
print(f'la lista de pares {lp}, {len(lp)}')
print(f'la lista de impares {li}, {len(li)}')