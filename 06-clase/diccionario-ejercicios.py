#crear lista con 3 usuarios y mostrar nombres
usuarios = [
    {'nombre': 'Juan', 'edad': 30},
    {'nombre': 'Maria', 'edad': 25},
    {'nombre': 'Pedro', 'edad': 25}
]
nombres = [u['nombre'] for u in usuarios]
print(nombres)

#crear una lista de diccionarios con autos
autos = []
op = 1
while op != 0:
    print('01 - Agregar auto')
    print('0 - Salir')
    op = int(input('Ingrese opcion: ')) 
    if op ==1:
        auto = {}
        auto['marca'] = input('Ingrese marca: ')
        auto['modelo'] = input('Ingrese modelo: ')
        auto['año'] = int(input('Ingrese año: '))
        autos.append(auto)
    elif op == 0:
        break
    else:
        print('Opcion invalida')

autos2016 = [auto for auto in autos if auto['año'] >= 2016]

for auto in autos2016:
    print(auto)
