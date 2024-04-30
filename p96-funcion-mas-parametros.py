def saluda(*nombres):
    print(f'saludos a: {nombres}')
    print(f'saludo especial a {nombres[0]}')
    for n in nombres:
         print(f'hola {n} bienvenido, nos da husto verte por aqui')

saluda('carlos','jose','pedro','luis','maria','teresa','santiag0',10,20)