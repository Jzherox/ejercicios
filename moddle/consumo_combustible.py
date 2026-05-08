#Consumo de combustible
#Pide los kilómetros recorridos y los litros de gasolina consumidos.
#Calcula el consumo por kilómetro.
km = float(input("Kilómetros recorridos: "))
litros = float(input("Litros consumidos: "))
consumo = litros / km
print(f"Consumo por kilómetro: {consumo:.2f} Litros")