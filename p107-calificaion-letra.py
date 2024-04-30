import os;
def caletra(prom):
    if prom>=90 and prom<100:
        return 'A', 'excelente'
    elif prom>=80 and prom<90:
        return 'B', 'bien'
    elif prom>=70 and prom<80:
        return 'C', 'suficiente'
    elif prom>=60 and prom<70:
        return 'D', 'deficiente'
    elif prom>=0 and prom<60:
        return 'F', 'reprobado'
    
os.system('cls')
prom = float(input('dame tu promedio'))
letra, mensaje = caletra(prom)
print(f'tu promedio de {prom} se le asigna la {letra} y es {mensaje}')