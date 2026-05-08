print("IVA")
p1=int(input("Ingrese el precio n1"))
p2=int(input("Ingrese el precio n2"))
p3=int(input("Ingrese el precio n3"))
iva = 0.15
total = p1+p2+p3
ivadescuento= total * iva
totaliva= total + ivadescuento
print("Precio total con un iva del 15 % : " , totaliva)