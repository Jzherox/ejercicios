# Solicita 4 notas de un estudiante y calcula el promedio - resultado con 2 decimales.

print("Calcular promedio de 4 notas")
nota1 = int(input("Ingresa la primera nota: "))
nota2 = int(input("Ingresa la segunda nota: "))
nota3 = int(input("Ingresa la tercera nota: "))
nota4 = int(input("Ingresa la cuarta nota: "))

promedio = (nota1 + nota2 + nota3 + nota4) / 4
print(f"El promedio es: {promedio:.2f}")