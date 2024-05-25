#tercer examen parcial
import os
class Jugador:
    def __init__(self, nombre, año, sexo, becado):
        self.nombre = nombre
        self.año = año
        self.sexo = sexo
        self.becado = becado
    def __str__(self):
        return f'Nombre: {self.nombre}, Año: {self.año}, Sexo = {self.sexo}, Becado: {'Becado' if self.becado else 'No becado'}'
    
class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = list()

    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)

    def calcularSubtotal(self):
        subtotal = 0
        for jugador in self.jugadores:
            if not jugador.becado:
                subtotal = subtotal + self.costo
        return subtotal
    def __str__(self):
        return f'>Nombre:    {self.nombre},      Rango: {self.rango},      Costo: {self.costo:.2f}'
    
class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = list()

    def agregarCategoria(self, categoria):
        self.categorias.append(categoria)
    def calcularTotales(self):
        totalcat = len(self.categorias)
        totalhom = 0
        totalmuj = 0
        total = 0
        for categoria in self.categorias:
            for jugador in categoria.jugadores:
                if jugador.sexo == 'Hombre':
                    totalhom = totalhom + 1
                elif jugador.sexo == 'Mujer':
                    totalmuj = totalmuj + 1
            total = total + categoria.calcularSubtotal()
        return totalcat, totalhom, totalmuj, total
    
def Reporte(academia):
    print('\nREPORTE DEL CLUB DEPORTIVO:\n')
    print(f'Nombre: {academia.nombre}')
    print(f'Propietario: {academia.propietario}')
    print(f'Domicilio: {academia.domicilio}\n')
    print(f'Total de categorias: {academia.totalcat}')
    print(f'Total de Hombres: {academia.totalhom}')
    print(f'Total de Mujeres: {academia.totalmuj}\n')
    print('>>Datos generales de las categorias:\n')
    for categoria in academia.categorias:
        print(f'{categoria}')
    print('\n>>Jugadores por categoria:')
    for categoria in academia.categorias:
        print(f'\n{categoria} - ({len(categoria.jugadores)})\n')
        for jugador in categoria.jugadores:
            print(f'{jugador}')
        subtotal = categoria.calcularSubtotal()
        print(f'\n-Subtotal: {subtotal:.2f}')
    print(f'\n-> Total: {academia.total:.2f}')
    
def main():
    jugador1 = Jugador('Alexander Lopez', 2006, 'Hombre', False)
    jugador2 = Jugador('Uriel Puga', 2007, 'Hombre', True)
    jugador3 = Jugador('Alejandra Escalona', 2008, 'Mujer', False)

    jugador4 = Jugador('Armando Santana', 2009,'Hombre', False)
    jugador5 = Jugador('Daniel Mijares', 2010,'Hombre', False)
    jugador6 = Jugador('Antonio Hernandez', 2011, 'Mujer', True)

    jugador7 = Jugador('Andrea Solis', 2012, 'Mujer', True)
    jugador8 = Jugador('Marissa Hernandes', 2013, 'Mujer', True)
    jugador9 = Jugador('Diana Soto', 2014, 'Mujer', False)

    categoria1 = Categoria('Junior A', '2006/2007/2008', 1250)
    categoria1.agregarJugador(jugador1)
    categoria1.agregarJugador(jugador2)
    categoria1.agregarJugador(jugador3)
    categoria2 = Categoria('Junior B', '2009/2010/2011', 850)
    categoria2.agregarJugador(jugador4)
    categoria2.agregarJugador(jugador5)
    categoria2.agregarJugador(jugador6)
    categoria3 = Categoria('Pony A', '2012/2013/2014', 700)
    categoria3.agregarJugador(jugador7)
    categoria3.agregarJugador(jugador8)
    categoria3.agregarJugador(jugador9)

    academia = Academia('Academia Santos Laguna', 'Francisco LoTo', 'Aguanaval 123, Hidraulica')
    academia.agregarCategoria(categoria1)
    academia.agregarCategoria(categoria2)
    academia.agregarCategoria(categoria3)
    academia.totalcat, academia.totalhom, academia.totalmuj, academia.total = academia.calcularTotales()
    Reporte(academia)
    
if __name__ == '__main__':
    os.system('cls')
    main()