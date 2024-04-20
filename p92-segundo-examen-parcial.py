import os; os.system('cls')

print('Muebleria Muebles Dico \nSistema de Procesamiento de Empleados')
grupo = []
print('Captura de datos de los empleados * para terminar:')

while True:
    datos = {}
    nombre = input('dame el nombre: ')
    if nombre!='*':
        datos['nombre'] = nombre
        datos['edad'] = int(input('edad: '))
        datos['sexo'] = (input('sexo: '))
        datos['sueldo'] = float(input('sueldo: '))
        grupo.append(datos)
    elif nombre == '*':
        break

print(f"Los datos como se guardan {grupo}")

print(f"Tabla de datos:\n")
for k in grupo[0].keys():
    print(f"{k:<15}",end="")
print("\r")
print("-"*60)

for empleados in grupo:
    for v in empleados.values():
       print(f"{v:<15}",end="")
    print("\r")
print("-"*60)

s=s2=0
for est in grupo:
    s=s+est["edad"]
for est in grupo:
    s2=s2+est["sueldo"]

print(f'Resumen\nEmpleados {len(grupo)}\nMujeres {grupo.count('m')}\nHombres {grupo.count('h')}\nEdad -> suma: {s}, Promedio {s/len(grupo)}\nSueldo -> suma: {s2}, Promedio {s2/len(grupo)}')
