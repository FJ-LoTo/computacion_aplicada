import os

class Empleado:
    def _init_(self,nombre,edad,sexo,casado,sueldo):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.casado=casado
        self.sueldo=sueldo
    def _str_(self):
        return f'nombre: {self.nombre}, edad: {self.edad}, sexo: {'mujer' if self.sexo=='M' else 'hombre'}, casado: {'casado(a)' if self.casado else 'soltero'}, sueldo: {self.sueldo}'

os.system('cls')
empleado01 = Empleado('jose diaz',35,'H',False,1200)
print('nombre: ',empleado01.nombre)
print('edad: ',empleado01.edad)
print('sexo: ',empleado01.sexo)
print('casado: ',empleado01.casado)
print('sueldo: ',empleado01.sueldo)
print(empleado01)

empleado02 = Empleado('Maria Lopez',40,'M',True,1400)
print(empleado02)

empleado03 = Empleado('Rocio Soto',45,'M',False,2000)
print(empleado03)

total = empleado01.sueldo+empleado02.sueldo+empleado03.sueldo
print('\nTOtal de sueldos: ',total)