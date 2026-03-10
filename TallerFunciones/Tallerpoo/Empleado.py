class Nomina:
    def calcular_total_pagar(self, valor_hora, horas_trabajadas, fondo_empleados,  otras_deducciones):
        salario_bruto = valor_hora  * horas_trabajadas
        total_deducciones = fondo_empleados + otras_deducciones
        salario_neto = salario_bruto - total_deducciones
        return salario_neto
    
nomina = Nomina()

while True:
    try:
        estado = input("¿El empleado esta activo? (s/n):").lower()

        if estado != "s":
            print("El empleado no esta activo. No se calcula la nomina.")
            break

        valor_hora = float(input("Ingrese el valor por hora: "))
        horas = float(input("Ingrese las horas trabajadas: "))
        fondo = float(input("Ingrese deduccion fondo de empleados: "))
        otras = float(input("Ingrese otras deducciones: "))

        total_pagar = nomina.calcular_total_pagar(valor_hora, horas, fondo, otras)

        print(f"Total a pagar en nomina: {total_pagar}")
        break
    except ValueError:
        print("Error: Ingrese solo valores numericos.")