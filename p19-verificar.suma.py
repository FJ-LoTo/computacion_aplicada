import os; os.system('cls')

print('verificando si la suma de dos numeros es igual a un tercero\n')
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 + n2 == n3:
    print(f'caso 1: {n1} + {n2} = {n3}')
elif n1 + n3 == n2:
    print(f'caso 2: {n1} + {n3} = {n2}')
elif n2 + n3 == n1:
    print(f'caso 3: {n2} + {n3} = {n1}')
elif n1 == n2 == n3:
    print(f'caso 4: {n1} = {n2} = {n3}')
else:
    print(f'caso 5: son diferentes y no suman')