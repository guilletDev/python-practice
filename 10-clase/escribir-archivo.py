#crear archivo y hacer un bucle para escribir nombres en el archivo siempre y cuando no sea salir, ya que al colocar salir sale del ciclo y se cierra el archivo
nombre_archivo = 'archivo.txt'
archivo = open(nombre_archivo, 'w')
while True:
    nombre = input("Ingrese un nombre (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break
    archivo.write(nombre + '\n')
archivo.close()



