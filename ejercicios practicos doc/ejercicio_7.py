# Cajero automático simple

import os

run = True
saldo = 1000

os.system('cls')
while run:
    print("\tCAJERO BANCARIO")
    print("Opciones disponibles:")
    print("1. Consultar saldo")
    print("2. Retirar efectivo")
    print("3. Salir")
    accion = int(input("\nIngresa una opcion: "))

    if accion == 1:
        print(f"Tienes un saldo de ${saldo}")
    elif accion == 2:
        if saldo >= 0:
            retiro = int(input("Ingresa la cantidad a retirar: "))
            if retiro < saldo:
                saldo = saldo - retiro
                print("Se ha realizado el retiro con exito")
            else:
                print("La cantidad a retirar excede su saldo")
    elif accion == 3:
        run = False
    else:
        print("\n\t*** Opcion invalida ***")
    input()
    os.system('cls')