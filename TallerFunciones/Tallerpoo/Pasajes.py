class Pasajes:
    def calcular_total(self, gastos):
        return sum(gastos)
    
pasajes = Pasajes()
gastos = []
dias = 1

print("Registro de gastos de pasajes (6 dias)")
print("=====================================")

while True:
    try:
        valor = float(input(f" Ingrese el gasto del dia {dias}:"))
        gastos.append(valor)
        dias += 1

        if dias > 6:
            break

    except ValueError:
        print("Error: debe ingresar un valor numerico.")

total = pasajes.calcular_total(gastos)

print("=====================================")
print(f"El total gastado en pasajes es: {total}")