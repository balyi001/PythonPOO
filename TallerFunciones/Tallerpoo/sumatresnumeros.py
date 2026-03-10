class Operaciones:
    def sumar_tres_numeros(self, a, b, c):
        suma = a + b + c
        return suma
    
op = Operaciones()

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))

resultado = op.sumar_tres_numeros(num1, num2, num3)

print("La suma de los tres numeros es: ", resultado)