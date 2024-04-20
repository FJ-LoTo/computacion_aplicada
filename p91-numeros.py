#conjuntos con numeros
import os; os.system('cls')

A = {50,60,70,80,90,100,200}
B = {60,90,100,300,400,500}
C = {10,20,60,90,70,100,600,700}

print(A,B,C)

print("\nUnion")
print("A union B",A | B)
print("\nUnion")
print("B union C",B | C)

print("\nDiferencia")
print("A diferencia c", A - C)

print("\nDiferencia simetrica")
print("B diferencia simetrica C", B ^ C)

print("\nInterseccion")
print("B interseccion C", B & C)

print("\nComprobamos subconjuntos")
print("A es subconjnto B", A.issubset(B))
print("C es subconjnto A", C.issubset(A))

print("\nVerificar")
print("100 esta en A", 100 in A)
print("60 esta en A, B y C", 60 in A, 60 in B, 60 in C)
print("900 no esta en C", 900 is not C)