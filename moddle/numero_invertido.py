invertido=""
for i in range(3):
    digitos=input(f"Ingrese {1+i} digitos por favor")
    for numero in digitos:
        invertido=numero+invertido

print(invertido)