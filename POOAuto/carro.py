class Carro:
    def __init__(self, marca, color, velocidad_max):
        self.marca = marca
        self.color = color
        self.velocidad = 0
        self.velocidad_max = velocidad_max
        self.encendido = False
        
    def encender(self):
        if not self.encendido:
            self.encendido = True
            return f"El {self.marca} esta encendido."
        return f"El {self.marca} ya esta encendido."
    
    def acelerar(self, aumento):
        if not self.encendido:
            return "No puedes acelerar, el auto esta apagado."
        
        if self.velocidad + aumento <= self.velocidad_max:
            self.velocidad += aumento
        else:
            self.velocidad = self.velocidad_max

        return f"Velocidad actual: {self.velocidad} km/h"
    
    def frenar(self):
        self.velocidad = 0
        return f"El {self.marca} se ha detenido."
    
    def __str__(self):
        return f"Carro {self.marca} de color {self.color}"