# 11. Mostrar un menú con opciones (1. Saludar, 2. Despedirse, 3. Salir). Repetir hasta elegir salir.

while True:
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("Hola")
    elif opcion == "2":
        print("Hasta luego")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opción no válida")

# 12. Generar un número aleatorio (1–50). Pedir intentos hasta adivinarlo.

import random
secreto = random.randint(1, 50)
intento = 0

while True:
    intento = int(input("Adivina el número (1-50): "))
    if intento < secreto:
        print("Es más alto")
    elif intento > secreto:
        print("Es más bajo")
    else:
        print("Adivinaste!")
        break

# 13. Pedir una contraseña hasta que coincida con una predefinida.

clave_correcta = "python123"
entrada = ""

while True:
    entrada = input("Ingresa la contraseña: ")
    if entrada != clave_correcta:
        print("Contraseña incorrecta, intenta de nuevo.")
    else:
        break
print("Acceso concedido.")

# 14. Solicitar un número entre 10 y 50 hasta que sea válido.

numero = 0
while True:
    numero = int(input("Ingresa un número entre 10 y 50: "))
    if numero < 10 or numero > 50:
        print("Fuera de rango.")
    else:
        break
print(f"Número válido: {numero}")

# 15. Permitir ingresar precios de productos hasta que el usuario decida terminar. Mostrar el total.

total = 0
continuar = "si"

while True:
    precio = float(input("Ingresa el precio del producto: "))
    total += precio
    continuar = input("¿Deseas ingresar otro producto? (si/no): ")
    if continuar.lower() == "no":
        break
print(f"El total de la compra es: {total}")