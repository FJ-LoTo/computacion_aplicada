def fac(n):
    for n in range(1,n+1):
        f=f+n
    return f

n = int(input('dame un numero y te doy du factorial'))
print(f'el factorial es {fac(n)}')