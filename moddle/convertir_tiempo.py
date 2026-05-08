#Conversión de tiempo
#Solicita una cantidad de minutos y conviértela a horas y minutos.
# Conversión de tiempo
minutos_totales = int(input("Ingresa los minutos: "))
horas = minutos_totales // 60
minutos = minutos_totales % 60
print(f"Resultado: {horas} horas y {minutos} minutos")