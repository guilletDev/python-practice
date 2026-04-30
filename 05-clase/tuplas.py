# crear una tupla con 3 numeros y mostrar la suma.
numeros = (1, 2, 3)
suma = sum(numeros)
print("La suma de los numeros es:", suma)

#otra forma de hacerlo
numeros = (1, 2, 3)
suma = 0
for numero in numeros:
    suma += numero  
print("La suma de los numeros es:", suma)
