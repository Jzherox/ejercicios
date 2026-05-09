# Ejercicios de Nivel Medio – Estructuras de Repetición en Python

# 1. Suma de números pares e impares
# Solicitar 10 números al usuario y mostrar:
# Suma de números pares
# Suma de números impares

suma_pares = 0
suma_impares = 0
for i in range(10):
    numero_ingresado = int(input("Ingresa un numero: "))
    if (numero_ingresado % 2) == 0:
        suma_pares += numero_ingresado
    else:
        suma_impares += numero_ingresado
print(f"La sumatoria de numeros pares es: {suma_pares}")
print(f"La sumatoria de numeros impares es: {suma_impares}")

# 2. Contador de positivos, negativos y ceros
# Pedir números hasta que el usuario escriba 999.
# Mostrar:
# Cantidad de positivos
# Cantidad de negativos
# Cantidad de ceros

cant_positivos = 0
cant_negativos = 0
cant_nulos = 0
while True:
    numero_ingresado = int(input("Ingresa un numero: "))
    if numero_ingresado == 999:
        break
    elif numero_ingresado > 0:
        cant_positivos += 1
    elif numero_ingresado < 0:
        cant_negativos += 1
    else:
        cant_nulos += 1

print("TOTAL NUMEROS ")
print(f"positivos: {cant_positivos}")
print(f"negativos: {cant_negativos}")
print(f"nulos: {cant_nulos}")

# 3. Tabla de multiplicar personalizada
# Pedir un número y mostrar su tabla desde el 1 hasta el número que el usuario indique.

numero = int(input("Ingresa un numero: "))
multiplo = int(input("¿Cuantas multiplicaciones tendra la tabla? "))
print(f"\t-- TABLA DE MULTIPLICAR DEL {numero} --")
for i in range(1, (multiplo + 1)):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")

# 4. Validación de contraseña
# Solicitar una contraseña hasta que:
# Tenga mínimo 8 caracteres
# Contenga al menos un número

contraseña_aprobada = False
while not contraseña_aprobada:
    contraseña_ingresada = input("Ingresa una contraseña: ")
    if len(contraseña_ingresada) < 8:
        print("La contraseña ingresada debe ser de minimo 8 caracteres")
        pass
    else:
        for letra_pos in range(len(contraseña_ingresada)):
            letra = contraseña_ingresada[letra_pos]
            if letra <= "9" and letra >= "0":
                print("Contraseña aprobada!")
                contraseña_aprobada = True
                break
        if not contraseña_aprobada:
            print("La contraseña debe tener un numero.")

# 5. Serie Fibonacci
# Mostrar los primeros n números de la serie Fibonacci.
# Ejemplo:
# 0 1 1 2 3 5 8 13

anterior, actual = 0, 1
numero = int(input("Ingresa un numero: "))

for i in range(0, numero):
    print(anterior)
    anterior, actual = actual, anterior + actual

# 6. Factorial de varios números
# Pedir cuántos números desea procesar y calcular el factorial de cada uno.

numero = int(input("Ingresa un numero: "))
factorial = numero
for i in range((numero - 1), 0, -1):
    factorial *= i

print(f"El factorial de {numero}, es: {factorial}")

# 7. Promedio de estudiantes
# Pedir:
# Cantidad de estudiantes
# Nombre y nota de cada uno
# Mostrar:
# Promedio general
# Mejor nota
# Peor nota

promedio = 0
mejor_nota = 0
peor_nota = 0

cant_estudiantes = int(input("Cantidad de estudiantes: "))
for i in range(cant_estudiantes):
    nombre_estu = input("Ingresa nombre del estudiantes: ")
    nota_estu = int(input("Ingresa nota del estudiantes: "))
    promedio += nota_estu
    if nota_estu < mejor_nota:
        peor_nota = nota_estu
    else:
        mejor_nota = nota_estu

promedio = promedio / cant_estudiantes
print(f"Promedio general: {promedio}")
print(f"Mejor nota: {mejor_nota}")
print(f"Peor nota: {peor_nota}")

# 8. Menú de operaciones matemáticas
# Crear un menú repetitivo:
# Sumar
# Restar
# Multiplicar
# Dividir
# Salir

while True:
    print("\tMENU OPERACIONES MATEMATICAS")
    print("1) sumar")
    print("2) restar")
    print("3) multiplicar")
    print("4) dividir")
    print("5) salir")
    opcion = int(input())

    if opcion == 5:
        break

    numero1 = int(input("Ingresa el primer numero: "))
    numero2 = int(input("Ingresa el segundo numero: "))
    
    match opcion:
        case 1:
            suma = numero1 + numero2
            print(f"SUMA: {numero1} + {numero2} = {suma}")
        case 2:
            resta = numero1 - numero2
            print(f"RESTA: {numero1} - {numero2} = {resta}")
        case 3:
            multiplicacion = numero1 * numero2
            print(f"MULTIPLICACION: {numero1} * {numero2} = {multiplicacion}")
        case 4:
            division = numero1 / numero2
            print(f"DIVISION: {numero1} / {numero2} = {division}")

# 9. Número primo
# Determinar si un número ingresado es primo.

es_primo = True
numero = int(input("Ingresa un numero: "))
if numero == 1:
    print("El numero 1 no es primo ni compuesto")
else:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(f"El numero {numero} no es primo")
            es_primo = False
            break
    if es_primo:
        print(f"El numero {numero} es primo")