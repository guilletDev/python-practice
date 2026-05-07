class usuario:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

#crear clase usuario y hace el password privado

class Usuario:
    def __init__(self, nombre, password):
        self.nombre = nombre
        self.__password = password

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def cambiar_password(self, nuevo_password):
        self.__password = nuevo_password    

    def mostrar_usuario(self):
        return f"Usuario: {self.nombre}"    


#ejericicio 3
#crear clase producto encapsulando el precio y validar no permitiendo el precio negativo           

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio
        else:
            print("El precio no puede ser negativo.")   

    def mostrar_producto(self):
        return f"Producto: {self.nombre}, Precio: {self.__precio}"

    print (Producto("Laptop", 1000).mostrar_producto())
