def calcular_total(subtotal, iva):
    return subtotal + iva

subtotal_venta = float(input("Ingrese el subtotal: "))
iva_venta = float(input("Ingrese el IVA: "))

total = calcular_total(subtotal_venta, iva_venta)

print(f"El total a pagar es: {total}")