#vemos conjuntos de python, son colecciones de elementos únicos, no ordenados y mutables.

#conjunto no tiene indice 
conjunto = {1, 2, 3, 4, 5}
conjunto.add(9)
print(conjunto)  #agregar un elemento al conjunto

#Crear un conjunto con 5 elementos y mostrarlo.

conjunto = {1, 2, 3, 4, 5}
print(conjunto) 
#Crear un conjunto con elementos repetidos y mostrarlo, se eliminaran los repetidos.
conjunto_repetidos = {1, 2, 2, 3, 4, 4, 5}
print(conjunto_repetidos)       
#Crear un conjunto con elementos de diferentes tipos y mostrarlo.
conjunto_diferentes = {1, 'Hola', 3.14, True}   
print(conjunto_diferentes)
#Crear un conjunto a partir de una lista y mostrarlo.
lista = [1, 2, 3, 4, 5]
conjunto_desde_lista = set(lista)
print(conjunto_desde_lista)


#Crear dos conjuntos y mostrar la intersección y la unión de ambos.
listaA = {5,6,4,2,7,3}
listaB = {1,2,4,2,7,9}
listaI = listaA & listaB
print ("numeros en comun ", listaI)
listaU = listaA | listaB
print("todos los numeros : " , listaU)

usuarios = []
#cant = int(input("ingrese cantidad de usuarios: "))
#for i in range(1,cant+ 1):
#    u = input("ingrese usuario : ")
#    usuarios.append(u)
# conjunto = set(usuarios)    
# print(conjunto)
op = 1
while op !=0:
    print("1 - añadir usuario")
    print("0 - mostar lista ")
    op = int(input("ingrese una opcion : "))
    if op == 1:
            u = input ("ingrese usuario : ")
            usuarios.append(u)
        elif op == 0:
            break
    else:
        print("opcion incorrecta!!!"
print("usuarios ingresados : ", set(usuarios))




