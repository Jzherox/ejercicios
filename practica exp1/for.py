# 6. Mostrar la tabla de multiplicar de un número ingresado por el usuario.

numero = int(input("Ingresa un numero: "))
multiplo = int(input("¿Cuantas multiplicaciones tendra la tabla? "))
print(f"\t-- TABLA DE MULTIPLICAR DEL {numero} --")
for i in range(1, (multiplo + 1)):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")

# 7. Calcular la suma de todos los números pares entre 1 y 100

sumatoria_pares = 0
for i in range(2, 101, 2):
    sumatoria_pares += i

print(f"Sumatoria total de numeros pares: {sumatoria_pares}")

# 8. Calcular el factorial de un número ingresado
