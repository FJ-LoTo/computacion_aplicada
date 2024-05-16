import os

class Rectangulo:
    def _init_(self,l,a):
        self.largo=l
        self.ancho=a
    def obtenerArea(self):
        return self.largo*self.ancho
    def obtenerPerimetro(self):
        return 2*self.largo + 2*self.ancho
    def _str_(self):
        return f'rectangulo[largo={self.largo} - ancho:{self.ancho}, Area={self.obtenerArea():.2f},circunferncia:{self.obtenerPerimetro():.2f}]'
    
os.system('cls')

r1=Rectangulo(12,3.4)
print('r1')
r2=Rectangulo(5.6,7.8)
print('r2')
r3=Rectangulo(10,10)
print('r3')

rectangulos=[]
rectangulos.append(r1)
rectangulos.append(r2)
rectangulos.append(r3)
rectangulos.append(Rectangulo(60,40))
print(rectangulos)


print('\ntodos de una vez', len(rectangulos))
for rectangulo in rectangulos:
    print(rectangulo)