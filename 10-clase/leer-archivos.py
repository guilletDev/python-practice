# leer archivo y mostrar su contenido whit open
nombre_archivo = 'archivo.txt'

archivo = open(nombre_archivo, 'r')
contenido = archivo.read()  
print(contenido)
archivo.close()

