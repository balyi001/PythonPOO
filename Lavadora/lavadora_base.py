import time
import os
from datetime import datetime
import winsound

class LavadoraBase:
    def __init__(self, kilos, tipo_ropa, estrato):
        self._kilos = kilos                 
        self._tipo_ropa = tipo_ropa.lower() 
        self.__estado = "apagada"           
        self._tiempo_lavado = 30            
        self._precio_kilo = 10000           
        self._iva = 0.19                    
        self._potencia_kw = 1.5             
        self._estrato = estrato             
        
        self.costo_base = 0
        self.costo_aumentado = 0
        self.costo_iva = 0
        self.energia_total = 0
        self.utilidad_empresario = 0

    def _barra_progreso(self, proceso, segundos=3):
        # Barra de carga técnica sin caracteres especiales
        print(f"\n{proceso}:")
        bar_size = 20
        for i in range(bar_size + 1):
            porcentaje = (i * 100) // bar_size
            relleno = "#" * i
            espacios = "-" * (bar_size - i)
            # \r permite sobrescribir la misma linea
            print(f"\r[{relleno}{espacios}] {porcentaje}%", end="")
            time.sleep(segundos / bar_size)
        print(" [OK]")

    def _play_audio(self, nombre_archivo):
        try:
            ruta_carpeta = os.path.dirname(__file__)
            ruta_audio = os.path.join(ruta_carpeta, "Sound", nombre_archivo)
            winsound.PlaySound(ruta_audio, winsound.SND_FILENAME | winsound.SND_NODEFAULT)
        except Exception:
            print(f"\n(Archivo de audio {nombre_archivo} no encontrado en carpeta Sound)")

    def encender(self):
        self.__estado = "encendida"
        print("\n--- PI-PI-PI ---")
        self._play_audio("encendido.wav") 
        print("Lava Smart: Sistema inicializado.")

    def _llenar(self):
        self._barra_progreso("Llenando tanque de agua", 2)
        self._play_audio("llenado.wav")

    def estregar(self):
        self._barra_progreso("Estregando prendas", 3)
        self._play_audio("lavado.wav")

    def enjuagar(self):
        self._barra_progreso("Ciclo de enjuague", 2)
        self._play_audio("enjuague.wav")

    def centrifugar(self):
        self._barra_progreso("Centrifugando", 2)
        self._play_audio("centrifugar.wav")

    def secar(self):
        self._barra_progreso("Secado termico", 3)
        self._play_audio("secado.wav")

    def lavar(self):
        pass

    def _calcular_costos(self):
        self.costo_base = self._kilos * self._precio_kilo
        prendas_especiales = ["interior", "pijamas", "vestidos"]
        if self._tipo_ropa in prendas_especiales:
            self.costo_aumentado = self.costo_base * 1.05
        else:
            self.costo_aumentado = self.costo_base
        self.costo_iva = self.costo_aumentado * 1.19
        self.utilidad_empresario = self.costo_aumentado * 0.30

    def _calcular_consumo_energia(self):
        kwh_operacion = self._potencia_kw * (self._tiempo_lavado / 60)
        tarifas = {2: 867.8, 3: 737.6, 4: 867.8, 5: 1041.0}
        tarifa_estrato = tarifas.get(self._estrato, 800)
        self.energia_total = kwh_operacion * tarifa_estrato
        self._play_audio("final.wav")

    def obtener_datos_reporte(self, nombre_cliente, modo):
        # Estructura para el Excel
        return {
            "Fecha_Hora": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            "Cliente": nombre_cliente,
            "Modo": modo,
            "Carga_KG": self._kilos,
            "Tipo_Ropa": self._tipo_ropa,
            "Total_Pago": round(self.costo_iva, 2),
            "Consumo_Energia": round(self.energia_total, 2)
        }

    def ciclo_terminado(self, nombre_cliente, modo):
        self._calcular_costos()
        self._calcular_consumo_energia()
        ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("\n" + "="*35)
        print("       REPORTE DE SERVICIO")
        print("="*35)
        print(f"Fecha/Hora: {ahora}")
        print(f"Cliente:    {nombre_cliente}")
        print(f"Modalidad:  {modo}")
        print(f"Total Neto: ${self.costo_iva:,.2f}")
        print("="*35)