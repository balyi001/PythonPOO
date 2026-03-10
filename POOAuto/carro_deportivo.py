# Importa la clase base 'Carro' desde un archivo/módulo llamado 'carro'
from carro import Carro

# Define la clase 'CarroDeportivo', que hereda todas las funciones de 'Carro'
class CarroDeportivo(Carro):
    def __init__(self, marca, color, velocidad_max, combustible):
        # Inicializa los atributos de la clase padre (marca, color, velocidad)
        super().__init__(marca, color, velocidad_max)
        # Atributo único para esta subclase: nivel de combustible específico
        self.combustible = combustible

    def acelerar(self, aumento):
        # Validación de seguridad: verifica si el motor está encendido (atributo de la clase padre)
        if not self.encendido:
            return f"El {self.marca} está apagado."
        
        # Validación de recursos: verifica si queda combustible antes de proceder
        if self.combustible <= 0:
            return "Sin combustible."

        # Lógica de alto rendimiento: multiplica el aumento solicitado para simular el modo turbo
        nitro = aumento * 2
        
        # Reutiliza la lógica de aceleración de la clase padre pasando el valor multiplicado
        mensaje_velocidad = super().acelerar(nitro)
        
        # Penalización de consumo: resta una cantidad fija de combustible por cada uso del turbo
        self.combustible -= 10
        
        # Corrección para evitar que el combustible muestre valores negativos
        if self.combustible < 0: 
            self.combustible = 0

        # Retorna el mensaje original de velocidad concatenado con el estado del combustible
        return f"{mensaje_velocidad} | Combustible: {self.combustible}L"

    def __str__(self):
        # Sobrescribe la representación del objeto para que sea legible al imprimirlo
        return f"Carro {self.marca} de color {self.color}"