class Operaciones:
    def sumar_tres_numeros(self, numeros):
        return sum(numeros)
    
op = Operaciones()
numeros = []

contador = 1
while contador <= 3:
    try:
        numero = float(input(f"Ingrese el numero {contador}:"))
        numeros.append(numero)
        contador += 1

    except ValueError:
        print("Error: Ingrese solo numeros")

resultado = op.sumar_tres_numeros(numeros)

print("La suma de los tres numeros es: ", resultado)