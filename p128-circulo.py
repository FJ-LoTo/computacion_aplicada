import os, math

class Circulo:
    def _init_(self,radio):
        self.radio=radio
    def obtenerArea(self):
        return math.pi*self.radio**2
    def obtenerCircunferencia(self):
        return 2**math.pi*self.radio
    def _str_(self):
        return f'circulo[radio={self.radio:.2f}, Area={self.obtenerArea():.2f},circunferncia:{self.obtenerCircunferencia():.2f}]'
    
os.system('cls')
print('\nprimer circulo')
circulo1=Circulo(10.40)
print(circulo1)
print(f'radio: {Circulo.radio:.2f}')
print(f'area : {circulo1.obtenerArea():.2f}')
print(f'circunf {circulo1.obtenerCircunferencia():.2f}')
print('\nsegundo circulo')
circulo2=Circulo(12.45)
print(circulo2)
