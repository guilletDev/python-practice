#polimorfismo es la capacidad de un objeto de tomar muchas formas. En programación orientada a objetos, el polimorfismo permite que una función o método pueda trabajar con objetos de diferentes clases, siempre y cuando compartan una interfaz común.
class Animal:
    def hacer_sonido(self):
        pass
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
# Crear instancias de Perro y Gato
perro = Perro()
gato = Gato()
# Llamar al método hacer_sonido para ambos objetos
print(perro.hacer_sonido())  # Salida: Guau
print(gato.hacer_sonido())   # Salida: Miau

#ejericicio 2
#crear clase figura con metodo area
#crear clase hija circulo y rectangulo que hereden de figura y calculen el area 
class circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio ** 2   

class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura  

circulo1 = circulo(5)
rectangulo1 = rectangulo(4, 6)

print(circulo1.area())     # Salida: 78.5
print(rectangulo1.area())   # Salida: 24    


#ejercicio 5 crear sistema de veiculos con clase padre vehiculo y clases hijas coche, moto, camion que hereden de vehiculo y tengan un metodo mostrar informacion que muestre el tipo de vehiculo y su velocidad maxima
#heerencia, polimorfismo (metodo mover()) y encapsulamiento (velocidad privada) 
class Vehiculo:
    def __init__(self, tipo, velocidad_maxima):
        self.tipo = tipo
        self.__velocidad_maxima = velocidad_maxima

    def get_velocidad_maxima(self):
        return self.__velocidad_maxima

    def mostrar_informacion(self):
        return f"Tipo de vehículo: {self.tipo}, Velocidad máxima: {self.__velocidad_maxima} km/h"       
class Coche(Vehiculo):
    def __init__(self, velocidad_maxima):
        super().__init__("Coche", velocidad_maxima)
class Moto(Vehiculo):
    def __init__(self, velocidad_maxima):
        super().__init__("Moto", velocidad_maxima)
class Camion(Vehiculo):
    def __init__(self, velocidad_maxima):
        super().__init__("Camión", velocidad_maxima)
coche1 = Coche(200)
moto1 = Moto(180)       
camion1 = Camion(120)
print(coche1.mostrar_informacion())  # Salida: Tipo de vehículo: Coche, Velocidad máxima: 200 km/h
print(moto1.mostrar_informacion())   # Salida: Tipo de vehículo: Moto, Velocidad máxima: 180 km/h
print(camion1.mostrar_informacion()) # Salida: Tipo de vehículo: Camión, Velocidad máxima: 120 km/h 





