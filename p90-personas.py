#conjuntos de personas y sus verificaciones
import os; os.system('cls')

A = {"Juan", "Maria", "Pedro", "Jose", "Rocio"}
B = {"Pedro", "Juan", "Pablo", "Mateo", "Esther"}

print(A,B)

print("\nUnion")
print("A union B",A | B)

print("\nInterseccion")
print("A interseccion B", A & B)

print("\nDiferencia")
print("A diferencia B", A - B)

print("\nDiferencia simetrica")
print("A diferencia simetrica B", A ^ B)

print("\nComprobamos subconjunto")
print("Pablo y Mateo es subconjunto B", {"Pablo", "Mateo"}.issubset(B))

print("\nComprobar superconjunto")
print("A es superconjunto Reynaldo y Angelica", A.issuperset({"Reynaldo", "Angelica"}))

print("\nVerificar")
print("Pedro esta en A", "Pedro" in A)
print("Lilia no esta en B", "Lilia" is not B)