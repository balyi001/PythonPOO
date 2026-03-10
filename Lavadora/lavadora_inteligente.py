from lavadora_base import LavadoraBase

class LavadoraInteligente(LavadoraBase):
    def __init__(self, kilos, tipo_ropa, estrato):
        super().__init__(kilos, tipo_ropa, estrato)
        self._wifi = True
        self._sensores = True

    def detectar_tipo_ropa(self):
        # Simula la accion de los sensores
        print(f"Sensores: Analizando tejido y suciedad de {self._tipo_ropa}...")

    def conectar_wifi(self):
        print("WiFi: Reporte de ciclo enviado a la nube.")

    def lavar(self):
        # Polimorfismo: Lavado optimizado
        print("Ejecutando lavado INTELIGENTE con ahorro de agua...")