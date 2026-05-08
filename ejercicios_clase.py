# Comparaciones lógicas entre variables numéricas
# Basado en image_bce61e.jpg
x = 5
y = 10

print(x == y)  # False
print(x != y)  # True
print(x < y)   # True
print(x >= 3)  # True

# Verificación de temperatura (IF simple)
# Basado en image_bce603.png y image_bce350.png
temperatura = 32
if temperatura > 30:
    print("Hace calor")

# Verificación de estado de usuario
# Basado en image_bce603.png
usuario_activo = True
if usuario_activo:
    print("Bienvenido al sistema")

# Control de stock de productos
# Basado en image_bce63d.jpg
stock = 0
if stock > 0:
    print("Producto disponible")
else:
    print("Producto agotado")

# Validación de mayoría de edad (Traducido de pseudocódigo)
# Basado en image_bce638.jpg
edad = 18 # Ejemplo de valor
if edad >= 18:
    print("Acceso permitido")
else:
    print("Acceso denegado")

# Evaluación de nota académica (Traducido de pseudocódigo)
# Basado en image_bce5fc.png
nota = 75 # Ejemplo de valor
if nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")

# Sistema de validación de contraseña
# Basado en image_bce63d.jpg
contraseña_maestra = "admin123"
entrada = input("Ingrese la contraseña: ")
if entrada == contraseña_maestra:
    print("Acceso concedido")
else:
    print("Acceso denegado")

# Simulación de estructura Switch-Case (Usando Match en Python 3.10+)
# Traducido de la sintaxis de JS/C en image_bce657.png
expresion = "valor1" # Ejemplo de valor
match expresion:
    case "valor1":
        print("Ejecutando instrucciones para valor1")
    case "valor2":
        print("Ejecutando instrucciones para valor2")
    case _:
        print("Instrucciones si no coincide ningún caso")

# Contador incremental con bucle While
# Basado en image_bce638.jpg
contador = 0
while contador < 5:
    print("Iteración", contador)
    contador += 1

# Cálculo de cuadrados con bucle For
# Basado en image_bce5fc.png
for i in range(1, 11):
    print(f"{i} al cuadrado es {i**2}")

# Bucle infinito con interrupción manual (Break)
# Basado en image_bce355.png
while True:
    opcion = input("¿Desea continuar? (s/n): ")
    if opcion.lower() != 's':
        break

# Clasificación de números pares e impares
# Basado en image_bce355.png
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")