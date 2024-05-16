def mayor(lista):
    m=lista[0]
    for n in range(len(lista)):
        if lista[n]>m:
            m = lista[n]
    return m

def menor(lista):
    m=lista[0]
    for n in range(len(lista)):
        if lista[n]<m:
            m = lista[n]
    return m

def promedio(lista):
    s=0
    for n in lista:
        s+=n
    return s/len(lista)