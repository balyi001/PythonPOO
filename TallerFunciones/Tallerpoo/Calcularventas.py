class Venta:
    def calcular_total(self, subtotal, iva):
        total = subtotal + iva
        return total
    
venta  = Venta()

subtotal = float(input("Ingrese el subtotal de la venta: "))
iva = float(input("Ingrese el valor del iva: "))

total = venta.calcular_total(subtotal, iva)

print("El total a pagar es: ", total)