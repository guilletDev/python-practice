# lista de objetos 
# crear una clase producto con atributos nombre, precio y stock
# crear una lista de productos y agregar productos a la lista
"""crear un menu para agregar productos a la lista y buscar productos por nombre"""

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
## main 
lista = []
op = 1
while op != 0:
    print("1 - agregar producto")
    print("2 - buscar producto")
    print("0 - salir")
    op = int(input("ingrese opcion: "))
    if op == 1:
        nombre = input("ingrese nombre = ")
        precio = input("ingrese precio = ")
        stock = input("ingrese stock = ")
        producto = Producto(nombre, precio, stock)
        lista.append(producto)
    elif op == 2:
        buscar = input("buscar producto: ")
        for prod in lista:
            if buscar in prod.nombre:
                print(f"nombre: {prod.nombre}, precio: {prod.precio}")