# Menu interactivo

# Crear un menú que simule controles:
# 1. Agregar dato
# 2. Mostrar datos
# 3. Salir

import os

run = True
datos = {}
os.system('cls')
while run:
    print("\tMEMORIA DE VARIABLES")
    print("Opciones disponibles:")
    print("1. Agregar datos")
    print("2. Mostrar datos")
    print("3. Salir")
    accion = int(input("\nIngresa una opcion: "))

    if accion == 1:
        nombre_var = input("Ingresa el nombre de la variable: ")
        valor_var = input("Ingresa el valor de la variable: ")
        datos[nombre_var] = valor_var
    elif accion == 2:
        if not datos:
            print('No hay variables registradas')
        else:
            print("VARIABLE - VALOR")
            for i in datos:
                print(f"{i} - {datos[i]}")
    elif accion == 3:
        run = False
    else:
        print("\n\t*** Opcion invalida ***")
    input()
    os.system('cls')