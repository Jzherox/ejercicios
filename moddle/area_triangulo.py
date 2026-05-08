# Pide la base y la altura de un triángulo y calcula su área.

print("Calcular area de un triangulo en cm²")
base = int(input("Ingresa base: "))
altura = int(input("Ingresa altura: "))

if base > 0 and altura > 0:
    area = (base * altura) / 2
    print(f"EL area de tu triangulo es de {area}cm²")
else:
    print("Los valores ingresados son invalidos")