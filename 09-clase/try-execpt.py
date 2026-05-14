#try-except 
# El bloque try se utiliza para envolver el código que puede generar una excepción, mientras que el bloque except se encarga de manejar esa excepción de manera controlada.
# En el bloque except, puedes especificar el tipo de excepción que deseas manejar, lo que te permite capturar y responder a errores específicos de manera adecuada.
# Ejemplo de uso de try-except:

try:    a = 10
    b = 0
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")   
try:    numero = int(input("Ingrese un número: "))
    print(f"El número ingresado es: {numero}")  
except ValueError:
    print("Error: Debe ingresar un número válido.") 
try:    lista = [1, 2, 3]
    print(lista[5])
except IndexError:  
    print("Error: Índice fuera de rango.")
try:    archivo = open("archivo_inexistente.txt", "r")
    contenido = archivo.read()
    print(contenido)
except FileNotFoundError:   
    print("Error: El archivo no existe.")


#ingresaar edad

try:    edad = int(input("Ingrese su edad: "))
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    print(f"Su edad es: {edad}")    

    