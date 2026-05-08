# Calculadora básica

numero_1 = int(input("Ingresa el primer numero: "))
numero_2 = int(input("Ingresa el segundo numero: "))

operacion = input("Ingresa el tipo de operacion a realizar (suma, resta, multiplicacion, division): ")

if operacion == "suma":
    resultado = numero_1 + numero_2
    print(f"{numero_1} + {numero_2} = {resultado}")
elif operacion == "resta":
    resultado = numero_1 - numero_2
    print(f"{numero_1} - {numero_2} = {resultado}")
elif operacion == "multiplicacion":
    resultado = numero_1 * numero_2
    print(f"{numero_1} * {numero_2} = {resultado}")
elif operacion == "division":
    resultado = numero_1 / numero_2
    print(f"{numero_1} / {numero_2} = {resultado}")
else:
    print("Operacion desconocida")
