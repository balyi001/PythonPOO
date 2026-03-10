class Venta: 
    def calcular_total(self, precio_unitario, cantidad):
        total = precio_unitario * cantidad
        return total
    
venta = Venta()

precio = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad vendida: "))

total_venta = venta.calcular_total(precio, cantidad)

print(f"El total de la venta es: {total_venta}")