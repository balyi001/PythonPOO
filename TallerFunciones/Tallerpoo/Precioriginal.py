class Descuento:
    def calcular_precio_con_descuento(self, precio_original, porcentaje_descuento):
        descuento = precio_original * (porcentaje_descuento / 100)
        precio_final = precio_original - descuento
        return precio_final
    
descuento = Descuento()

precio = float(input("Ingrese el precio original: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))

precio_con_descuento = descuento.calcular_precio_con_descuento(precio, porcentaje)

print(f"El precio final con descuento es: {precio_con_descuento}")