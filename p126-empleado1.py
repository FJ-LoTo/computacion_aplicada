import os

class Empleado:
    def _init_(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def _str_(self):
        return f'nombre: {self.nombre} - edad: {self.edad}\n'
    
os.system('cls')
empleado01= Empleado('Jose Diaz', 35)
print('nombre: ',empleado01.nombre)
print('edad: ',empleado01.edad)
empleado01.edad=40
print(empleado01)

empleado02 = Empleado('Sandra Lopez',22)
print(empleado02)

empleado03 = Empleado('Lucia Ramirez',15)
print(empleado03)

print(f'promedio de edad de los 3', (empleado01.edad + empleado02.edad + empleado03.edad)/3)