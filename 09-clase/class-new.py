# clases de libros como harry potter
class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_informacion(self):
        return f"'{self.titulo}' por {self.autor}, publicado en {self.año_publicacion}" 
libro1 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", 1997)
print(libro1.mostrar_informacion())  # Salida: 'Harry Potter y la piedra filosofal' por J.K. Rowling, publicado en 1997

