#crear clase cuenta bancaria atributos: titular, saldo
#metodo: depositar, retirar, mostrar saldo
class CuentaBancaria:
    def __init__(self, titular, saldo):                             
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito de {monto} realizado. Nuevo saldo: {self.saldo}")
    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= monto
            print(f"Retiro de {monto} realizado. Nuevo saldo: {self.saldo}")

            







#ejericicio 4 
#crear clase producto atribbutos: nombre, precio, cantidad
#metodo: calcular valor total del producto (precio * cantidad)  

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def valor_total(self):
        return self.precio * self.cantidad