# Importación de la clase base 'Carro' desde el módulo externo
from carro import Carro

# Definición de la subclase que hereda las propiedades de Carro
class CarroHibrido(Carro):
    def __init__(self, marca, color, velocidad_max, bateria, gasolina):
        # Llamada al constructor de la clase padre (Carro) para inicializar atributos básicos
        super().__init__(marca, color, velocidad_max)
        # Atributos específicos del modelo híbrido
        self.bateria = bateria
        self.gasolina = gasolina

    def acelerar(self, aumento):
        # Validación: El coche no puede acelerar si no ha sido encendido previamente
        if not self.encendido:
            return f"El {self.marca} está apagado."
        
        # Lógica de cambio de sistema: Prioriza el uso de la fuente de energía más abundante
        if self.bateria > self.gasolina:
            # Si hay más batería, consume energía eléctrica
            uso = "Usando batería"
            self.bateria -= 5
            porcentaje = f"({self.bateria}%)"
        elif self.gasolina > self.bateria:
            # Si hay más gasolina, consume combustible fósil
            uso = "Usando gasolina"
            self.gasolina -= 5
            porcentaje = f"{self.gasolina}L"
        else:
            # Caso en el que ambos niveles están en 0 o son iguales y no hay suficiente para operar
            return "Sin energía (batería y gasolina agotadas)."

        # Ejecuta la lógica original de aceleración de la clase padre y guarda el mensaje
        mensaje_velocidad = super().acelerar(aumento)
        # Retorna el estado combinado: incremento de velocidad + fuente de energía utilizada
        return f"{mensaje_velocidad} | {uso} {porcentaje}"

    def __str__(self):
        # Representación en cadena de texto del objeto para facilitar su lectura en un print
        return f"Carro {self.marca} de color {self.color}"