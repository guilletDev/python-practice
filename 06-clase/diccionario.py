#diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

print(persona)

#modificar
persona["nombre"] = "Maria"
print(persona)

#agregar un nuevo campo (email)
persona["email"] = "maria@gmail.com"
print(persona)

#recorrer diccionario
persona = {'nombre': 'Pedro', 'edad': 25}
for key, value in persona.items():
    print(key, value)

#lista de diccionarios
personas = [
    {'nombre': 'Juan', 'edad': 30},
    {'nombre': 'Maria', 'edad': 25},
    {'nombre': 'Pedro', 'edad': 25}
]   

for persona in personas:
    print(f"{persona['nombre']}, tiene {persona['edad']} años")

#iterar sobre la lista de diccionarios
for persona in personas:
    print(persona['nombre'], persona['edad'])


#acceder a un valor especifico
print(personas[0]['nombre'])

#anadir un nuevo diccionario a la lista
personas.append({'nombre': 'Ana', 'edad': 28})
print(personas)

#eliminar un diccionario de la lista
personas.remove({'nombre': 'Juan', 'edad': 30})
print(personas)

#compresion de lista para mostrar edades mayor a 18
edades_mayores = [persona['edad'] for persona in personas if persona['edad'] > 18]
print(edades_mayores)

#otro ejemplo
personas_mayores = [p for p in personas if p['edad'] > 18]
print(personas_mayores)


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






