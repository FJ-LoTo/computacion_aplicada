import os

class Articulo:
    def _init_(self,id,descripcion,cantidad,precio):
        self.id=id
        self.descripcion=descripcion
        self.cantidad=cantidad
        self.precio=precio
    def obtenerTotal(self):
        return self.cantidad*self.precio
    def _str_(self):
        return f'Articulo: [ID: {self.id}, Descripcion: {self.descripcion}, Cantidad: {self.cantidad}, Precio: {self.precio}]'

os.system('cls')
# Programa principal
art1 = Articulo('A101', 'Pluma Roja', 888, 0.08)
print(art1)
art1.cantidad = 999
art1.precio = 0.99
print("id = ",art1.id)
print("descripcion = ",art1.descripcion)
print("cantidad = ",art1.cantidad)
print("precio = ",art1.precio)
print("total = ",art1.obtenerTotal())
art2 = Articulo("A102", "Pluma Azul", 934, 1.2)
print(art2)
art3 = Articulo("P103", "Lapiz del 12", 456, 0.5)
print(art3)
total = art1.obtenerTotal() + art2.obtenerTotal() + art3.obtenerTotal()
print('Total todos:', total)