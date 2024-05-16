import os
def procesa(n1,n2):
    todos=[]
    cuenta=[]
    todos.extend(n1)
    todos.extend(n2)
    todos.sort
    for i in range(len(todos)):
        todos[i] = todos[i].upper()
        cuenta.append(len(todos[i]))
    return todos,cuenta

def entra():
    noms=[]
    while True:
        n=input('nombre? ')
        if n=='' : break
        noms.append(n)
    return noms

os.system('cls')
noms1 = ['juan','pedro','luis','jose','maria']
#noms2 = ['kucia','angelica','miguel','sandra']
noms2 = entra()

nombres,cuenta = procesa(noms1,noms2)

print(f'nombres 1: {noms1}, {len(noms1)}')
print(f'nombres 2: {noms2}, {len(noms2)}')
print(f'nombres : {nombres}, {len(nombres)}')
print(f'cuenta : {cuenta}, {len(cuenta)}')