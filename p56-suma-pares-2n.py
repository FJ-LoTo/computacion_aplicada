#suma numeros pares y su suma
import os; os.system('cls')

n = int(input('hasta donde deseas los numeros? '))

s=0
print('numeros pares y su suma')
for i in range (2,n+1,2):
        print(i,end=' ')
        s=i+s
print('la suma es ',s)