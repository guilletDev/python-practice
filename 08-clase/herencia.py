#crear clase persona y clase hija alumno
#crear metodo presentarse 
#alumno hereda y muestra un mensaje con su nombre y grado

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

class Alumno(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        return f"{self.presentarse()} Estoy en el grado {self.grado}."

# Crear una instancia de Alumno
alumno1 = Alumno("Juan", 20, "10mo grado")
# Llamar al método mostrar_grado
print(alumno1.mostrar_grado())  
