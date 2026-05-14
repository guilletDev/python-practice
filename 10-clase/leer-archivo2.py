#leer archivo y contar lineas   

# Abrir el archivo en modo lectura
archivo = open('archivo.txt', 'r')
lineas = archivo.readlines()
print(f"Número de líneas: {len(lineas)}")
# Cerrar el archivo
archivo.close()

