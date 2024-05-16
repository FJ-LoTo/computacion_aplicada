import p120modulofunciones as p120
import math
import os

def leer():
    lista = []
    while (True):
        n = int(input("Dame un numero: "))
        if n ==-1: break
        lista.append(n)
    return lista

def varianza(lista):  
    media = sum(lista)/len(lista)
    varianza = sum((x-media)**2 for x in lista)/(len(lista)-1)
    return math.sqrt(varianza)

os.system('cls')

lista = leer()
print("Lista de numeros: ",lista)

men = p120.menor(lista)
may = p120.mayor(lista)
prom = p120.promedio(lista)
print("El menor es: ", men)
print("El mayor es: ", may)
print(f"La media es: {prom:.2f}")
var = varianza(lista)
print(f"La varianza es: {var:.2f}")
desv = math.sqrt(var)
print(f"La desviacion estanndar es: {desv}")