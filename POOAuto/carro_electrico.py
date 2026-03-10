from carro import Carro

class CarroElectrico(Carro):
    def __init__(self, marca, color, velocidad_max, bateria_max):

        # super llama al constructor de la clase padre
        super().__init__(marca, color, velocidad_max)
        self._bateria = bateria_max
        self.bateria_max = bateria_max
    
    def recargar(self):
        self._bateria = self.bateria_max
        return "Bateria cargada al 100%"
    
    # Polimorfismo
    def acelerar(self, aumento):
        if not self.encendido:
            return "El carro esta apagado, enciendalo primero."
        
        if self._bateria <= 0:
            return "Bateria agotada, no puedes acelerar"
        
        mensaje_velocidad = super().acelerar(aumento)

        self._bateria -= 5

        return f"{mensaje_velocidad} | Bateria:{self._bateria}%"
