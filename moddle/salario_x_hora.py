print("SALARIO")
hora=int(input("Ingrese el total de horas trabajadas : "))
pago=int(input("Ingrese el pago por hora : "))
descuento=0.10
pagototal=hora*pago
descontar = pagototal * descuento
pagodescontar= pagototal - descontar
print("DIA DE PAGA POR EL TRABAJO REALIZADO")
print("TOTAL DE PAGO : " , pagototal)
print ("DESCUENTO DEL 10 % : " , pagodescontar)