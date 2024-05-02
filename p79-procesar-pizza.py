import os; os.system('cls')

ingr = {'T':1.50,'P':3.50,'C':3.74,'A':0.40}
base = 15
st = 0
tot = 0

pedido = input('ingredientes de tu pizza? ').upper()
for i in pedido:
    if i in 'PTCA':
        st = st+ingr[i]
st = st+base

if st>=20:
    tot = st-(st*0.05)


print(f'el subtotal es {st}')
print(f'\nel total es {tot}') 