# # 6. Mostrar la tabla de multiplicar de un número ingresado por el usuario.

# numero = int(input("Ingresa un numero: "))
# multiplo = int(input("¿Cuantas multiplicaciones tendra la tabla? "))
# print(f"\t-- TABLA DE MULTIPLICAR DEL {numero} --")
# for i in range(1, (multiplo + 1)):
#     resultado = numero * i
#     print(f"{numero} * {i} = {resultado}")

# # 7. Calcular la suma de todos los números pares entre 1 y 100

# sumatoria_pares = 0
# for i in range(2, 101, 2):
#     sumatoria_pares += i

# print(f"Sumatoria total de numeros pares: {sumatoria_pares}")

# # 8. Calcular el factorial de un número ingresado

# numero = int(input("Ingresa un numero: "))
# factorial = numero
# for i in range((numero - 1), 0, -1):
#     factorial *= i

# print(f"El factorial de {numero}, es: {factorial}")

# # 9. Contar cuántas veces aparece una letra específica en una palabra.

# palabra = input("Ingresa una palabra: ")
# letra = input("Ingresa una letra: ")
# veces = 0
# for i in range(len(palabra)):
#     if letra == palabra[i]:
#         veces += 1

# print(f"La letra -{letra}- se repite {veces} veces")

# 10. Mostrar la serie: 2, 4, 6, 8, ..., hasta n términos.

numero = int(input("Ingresa cantidad de terminos: "))
lista_numerica = ""
for i in range(2, ((numero * 2) + 1), 2):
    lista_numerica += f"{i}, "

lista_numerica = lista_numerica[:-2]
print(f"lista numerica de {numero} terminos: {lista_numerica}")