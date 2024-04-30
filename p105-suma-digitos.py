def sumadigitos(n):
    suma=0
    while n!=0:
        dig = n%10
        sum=sum+dig
        n=n//10
    return suma

n=int(input('dame un numero entero y sumo sus digitos'))
print(f'el numero es {n} y la suma es {sumadigitos(n)}')