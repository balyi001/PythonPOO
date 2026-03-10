class Inventario:
    def calcular_saldo_final(self, saldo_inicial, cantidades_compradas, cantidades_vendidas, cantidad_dada_de_baja):
        saldo_final = saldo_inicial + cantidades_compradas - cantidades_vendidas - cantidad_dada_de_baja
        return saldo_final
    
inventario = Inventario()

saldo_inicial = int(input("Ingrese el saldo inicial del mes: "))
compradas = int(input("Ingrese las cantidades compradas: "))
vendidas = int(input("Ingrese las cantidades vendidas: "))
dadas_baja = int(input("Ingrese la cantidad dada de baja: "))

if saldo_inicial <= 0:
    print("No hay suficiente Inventario,")

saldo_final = inventario.calcular_saldo_final(saldo_inicial, compradas, vendidas, dadas_baja)

print(f"El saldo final del inventario es: {saldo_final}")