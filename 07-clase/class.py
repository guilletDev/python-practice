class mascota:
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
    def descripcion(self):
        return f"{self.nombre} es un {self.tipo} de {self.edad} años."

# Crear una instancia de la clase mascota
mi_mascota = mascota("Fido", "perro", 5)

# Llamar al método descripcion
print(mi_mascota.descripcion())

# Crear otra instancia de la clase mascota
otra_mascota = mascota("Mittens", "gato", 3)

# Llamar al método descripcion
print(otra_mascota.descripcion())
        
