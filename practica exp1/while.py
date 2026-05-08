# 1. Mostrar los números del 1 al 20 usando while

numero = 0
lista_numerica = ""
while True:
    numero += 1
    lista_numerica += f"{numero}, "
    if numero == 20:
        lista_numerica = lista_numerica[:-2]
        break
    
print(f"lista numerica ascendente (1 - 20): {lista_numerica}")

# 2. Mostrar los números del 20 al 1.

numero = 20
lista_numerica = ""
while True:
    lista_numerica += f"{numero}, "
    numero -= 1
    if numero == 0:
        lista_numerica = lista_numerica[:-2]
        break

print(f"lista numerica descendente (20 - 1): {lista_numerica}")

# 3. Pedir números al usuario hasta que ingrese 0. Mostrar la suma total

sumatoria = 0
while True:
    numero = int(input("Ingresa un numero (0 para terminar): "))
    if numero == 0:
        break
    sumatoria += numero

print(f"sumatoria total: {sumatoria}")

# 4. Solicitar números hasta que el usuario ingrese un número negativo. Calcular el promedio.

promedio = 0
cant_numeros = 0
while True:
    numero = int(input("Ingresa un numero (negativo para terminar): "))
    if numero < 0:
        break
    promedio += numero
    cant_numeros += 1

try:
    promedio = promedio / cant_numeros
    print(f"sumatoria total: {promedio}")
except:
    print("No se ingresaron numeros a promediar")

# 5. Pedir un número positivo. Repetir hasta que el usuario ingrese un valor válido.

while True:
    numero = int(input("Ingresa un numero positivo: "))
    if numero >= 1:
        break

print(f"El numero ingresado fue: {numero}")