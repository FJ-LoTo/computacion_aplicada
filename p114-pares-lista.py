def pares(lista):
    p = []
    for n in lista:
        if n%2 == 0:
            p.append(n)
    return p

numeros = [1,2,3,4,5,6,7,8,9,10]
res = pares(numeros)
print(f'los pares son {res} y son {len(res)} ')