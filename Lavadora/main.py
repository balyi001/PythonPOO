import pandas as pd
import random
from datetime import datetime
from lavadora_estandar import LavadoraEstandar
from lavadora_inteligente import LavadoraInteligente

class SistemaLavaSmart:
    def __init__(self):
        self.clientes_totales = 0
        self.facturacion_global = 0
        self.historial_servicios = []

    def solicitar_dato(self, mensaje, tipo, validacion=None):
        while True:
            dato = input(f"{mensaje} (o 'OFF' para cancelar): ")
            if dato.upper() == "OFF": return "CANCELAR"
            try:
                valor = tipo(dato)
                if validacion and not validacion(valor):
                    print("Dato fuera de rango.")
                    continue
                return valor
            except ValueError:
                print("Error: Ingrese un valor numerico valido.")

    def ejecutar(self):
        print("\n--- BIENVENIDO A LAVA SMART 2026 ---")
        nombre_cli = input("Nombre del cliente: ")
        
        print("\nSeleccione tipo de servicio:")
        print("1. Lavado Estandar")
        print("2. Lavado Inteligente (Autodeteccion)")
        sel = self.solicitar_dato("Opcion", int, lambda x: x in [1, 2])
        if sel == "CANCELAR": return

        if sel == 2: # Lavadora Inteligente: Sensores de peso y ropa
            kilos = round(random.uniform(5, 40), 1)
            prenda = random.choice(["interior", "pijamas", "vestidos", "otra"])
            modo_texto = "Inteligente"
            print(f"\n[SENSORES]: Peso detectado: {kilos}kg | Ropa detectada: {prenda}")
        else: # Lavadora Estandar: Manual
            kilos = self.solicitar_dato("Ingrese kilos (5-40)", float, lambda x: 5 <= x <= 40)
            if kilos == "CANCELAR": return
            
            opciones = {1: "interior", 2: "pijamas", 3: "vestidos", 4: "otra"}
            print("\nTipos de ropa disponibles:")
            for k, v in opciones.items(): print(f"{k}. {v}")
            idx = self.solicitar_dato("Opcion de ropa", int, lambda x: x in opciones)
            if idx == "CANCELAR": return
            prenda = opciones[idx]
            modo_texto = "Estandar"

        estrato = self.solicitar_dato("Ingrese estrato (2-5)", int, lambda x: 2 <= x <= 5)
        if estrato == "CANCELAR": return

        # Instanciar el equipo segun la seleccion
        if sel == 1:
            equipo = LavadoraEstandar(kilos, prenda, estrato)
        else:
            equipo = LavadoraInteligente(kilos, prenda, estrato)
        
        # Inicio de procesos visuales
        equipo.encender()
        if sel == 2: equipo.detectar_tipo_ropa()
        
        equipo._llenar()
        equipo.estregar()
        equipo.lavar()
        equipo.enjuagar()
        equipo.centrifugar()
        
        if input("\nDesea incluir secado? (s/n): ").lower() in ['s', 'si']:
            equipo.secar()

        # Finalizacion y almacenamiento
        equipo.ciclo_terminado(nombre_cli, modo_texto)
        self.historial_servicios.append(equipo.obtener_datos_reporte(nombre_cli, modo_texto))
        
        self.clientes_totales += 1
        self.facturacion_global += equipo.costo_iva
        
        if isinstance(equipo, LavadoraInteligente):
            equipo.conectar_wifi()

    def finalizar_jornada(self):
        if self.historial_servicios:
            # Exportacion a Excel
            df = pd.DataFrame(self.historial_servicios)
            nombre_archivo = f"Reporte_LavaSmart_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
            df.to_excel(nombre_archivo, index=False)
            print(f"\n[SISTEMA]: Datos exportados correctamente a {nombre_archivo}")

if __name__ == "__main__":
    app = SistemaLavaSmart()
    while True:
        app.ejecutar()
        op = input("\nAtender nuevo cliente? (s/n): ").lower()
        if op in ['n', 'no']:
            app.finalizar_jornada()
            print("Cerrando sistema administrativo.")
            break