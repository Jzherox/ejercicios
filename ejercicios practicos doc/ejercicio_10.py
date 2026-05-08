# Validación de campos

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

if not nombre or edad <= 0:
    print("Error: El nombre no puede estar vacío y la edad debe ser mayor a 0.")
else:
    print(f"Hola {nombre}, tienes {edad} años.")