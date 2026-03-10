class Producto:
    def calcular_ganacia(self, costo_unitario, precio_venta):
        ganancia = precio_venta - costo_unitario
        return ganancia
    
producto = Producto()

costo = float(input("Ingrese el costo unitario: "))
precio = float(input("Ingrese el precio de la venta: "))

ganancia = producto.calcular_ganacia(costo, precio)

print(f"La ganancia obtenida es: {ganancia}")