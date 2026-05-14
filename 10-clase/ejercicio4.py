#crear sistema de notas 
#crear un archivo llamado notas.txt y escribir 3 tareas que tenga que hacer, luego leer el archivo y mostrar su contenido
with open('notas.txt', "w") as file:
    file.write('estudiar para el examen\n')
    file.write('hacer ejercicio de python\n')
    file.write('leer el libro de python\n')
#leer el archivo y mostrar su contenido     
with open('notas.txt', "r") as file:
    notas = file.read()
    print(notas)

