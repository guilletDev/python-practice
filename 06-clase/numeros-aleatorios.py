#numeros aleatorios
import random

#generar un numero aleatorio entre 1 y 10
numero = random.randint(1, 10)
print(numero)

#numero entero aleatorio entre 1 y 100
numero = random.randint(1, 100)
print(numero)

#numero decimal aleatorio entre 0.0 y 1.0
decimal = random.random()
print(decimal)

#simular un dado entre 1 y 6
dado = random.randint(1, 6)
print(dado)

#simular una moneda
moneda = random.choice(["cara", "cruz"])
print(moneda)

#generar lista de numeros aleatorios y calcular promedio
n= int(input('ingrese tamano de la lista: '))
numeros = []
cont = 0
for i in range(0, n):
    numeros.append(random.randint(1, 100))

print(numeros)

cont = 0 
for i in range(0, n):
    cont += numeros[i]

print("promedio:", cont/n)

