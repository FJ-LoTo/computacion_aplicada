#promedio calificaciones
import os; os.system('cls')

print('Dame 5 calificaciones separadas por un espacio\n')
n1, n2, n3, n4, n5 = input().split()
n1, n2, n3, n4, n5= int(n1), int(n2), int(n3), int(n4), int(n5)
promedio = (n1+n2+n3+n4+n5)/5
print(f'tu promedio es {promedio:.2f}')

if promedio>0 and promedio<6:
        print(f'Quedas reprobado')
elif promedio>=6 and promedio<7:
        print(f'pasas de panzaso')
elif promedio>=7 and promedio<8:
        print(f'muy bien, puedes mejorar')
elif promedio>=8 and promedio<9:
        print(f'excelente, sigue así')
elif promedio>=9 and promedio<=10:
        print(f'Perfecto, tu esfuerzo valió la pena')
        