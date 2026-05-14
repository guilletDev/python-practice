#rutas y directorios
import os
#obtener ruta actual
ruta_actual = os.getcwd()
print(f"Ruta actual: {ruta_actual}")
#cambiar de directorio
os.chdir('..')
ruta_actual = os.getcwd()
print(f"Ruta actual después de cambiar: {ruta_actual}")
#crear un nuevo directorio
nuevo_directorio = 'nuevo_directorio'
os.mkdir(nuevo_directorio)
print(f"Directorio '{nuevo_directorio}' creado.")

