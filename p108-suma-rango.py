import os;
def sumarango(ini,fin):
    s=0
    for i in range(ini,fin + 1):
        s=s+i
    return s

os.system('cls')
while True:
    i = int(input('dame inicio'))
    f = int(input('dame fin'))
    if i<f:
        break

print(f'la suma del rango {i}..{f} = {sumarango(i,f)}')