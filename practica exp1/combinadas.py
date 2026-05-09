# 16. Mostrar tablas del 1 al 10 usando ciclos anidados.

for i in range(1, 11):
    print(f"\nTabla del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

# 17. Mostrar una pirámide invertida de asteriscos según un número ingresado.

n = int(input("Ingresa el tamaño de la pirámide: "))
for i in range(n, 0, -1):
    nivel = (((" " * n))[:-(i)] + ("*" * i)) + ("*" * (i-1))
    print(nivel)

# 18. Mostrar todos los números primos entre 1 y 100.

print("Números primos entre 1 y 100:")
for num in range(2, 101):
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num, end=" ")

# 19. Adivinar un número con máximo 5 intentos. Indicar si el número es mayor o menor.

import random
secreto = random.randint(1, 50)
intentos_restantes = 5

while intentos_restantes > 0:
    print(f"\nTienes {intentos_restantes} intentos.")
    intento = int(input("Adivina el número (1-50): "))
    
    if intento == secreto:
        print("¡Ganaste! Adivinaste el número.")
        break
    elif intento < secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    
    intentos_restantes -= 1

if intentos_restantes == 0:
    print(f"\nPerdiste. El número era {secreto}.")

# 20. Crear una matriz de n x m con valores ingresados por el usuario y mostrar la suma de cada fila.

n = int(input("Ingresa número de filas (n): "))
m = int(input("Ingresa número de columnas (m): "))
matriz = []

for i in range(n):
    fila = []
    for j in range(m):
        valor = int(input(f"Valor para [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)

print("\nResultados:")
for i in range(n):
    suma_fila = sum(matriz[i])
    print(f"Suma de la fila {i + 1}: {suma_fila}")