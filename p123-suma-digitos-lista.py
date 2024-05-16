import os
def leer():
    lista = []
    while (True):
        n = int(input('Dame un numero: '))
        if n ==-1: break
        lista.append(n)
    return lista

def sumdigitos(n):
    suma = 0
    while n!=0:
        dig = n % 10
        suma = suma + dig
        n = n//10
    return suma

def suma_digitos_lista(lista):
    sumaT = []
    for numero in lista:
        sumaeach = sumdigitos(numero)
        sumaT.append(sumaeach)
    return sumaT
os.system('cls')
lista = leer()
print("La lista es: ", lista)
res = suma_digitos_lista(lista)
print(f"La suma de digitos de numeros es: {res}")