# Simulación de consola

import sys, os

os.system("cls")

run_consola = True
pila_comandos = {"hola" : "Saludos usuario.", 
                 "lenguaje" : f"ejecutando programa con el lenguaje python.",
                 "version" : f"version actual del lenguaje: {sys.version}"}

while run_consola:
    entrada = input("<usuario>: ")

    if entrada in pila_comandos:
        print(f"<consola>: {pila_comandos[entrada]}")
        pass
    elif entrada == "limpiar":
        os.system("cls")
    elif entrada == "salir":
        print(f"<consola>: cerrando consola...")
        run_consola = False
    else:
        print(f"<consola>: comando desconocido.")
        pass
