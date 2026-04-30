#Crear una lista de 5 numeros y mostrarlo.
numeros = [1, 2, 3, 4, 5]
print(numeros)

#Crear lista de nuemero que ingrese el usuario y mostrarlo siempre y cuando no sea 0, cuando sea 0 sale del ciclo while. 
numeros_usuario = []
while True:
    numero = int(input("Ingrese un numero (0 para salir): "))
    if numero == 0:
        break
    numeros_usuario.append(numero)  
print("Numeros ingresados por el usuario:", numeros_usuario)

#OTRA Opcion
n=1
numeros= []
while n != 0:
    n = int(input("Ingrese un numero: "))
    if n != 0:
        numeros.append(n)

print("Numeros ingresados por el usuario:", numeros)  

