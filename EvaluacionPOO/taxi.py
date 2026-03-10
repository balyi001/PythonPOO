from vehiculo import Vehiculo

class Taxi(Vehiculo):
  def  __init__(self, marca, modelo, precio_alquiler, tarifa_por_km):
    super().__init__(marca, modelo, precio_alquiler)
    self.__tarifa_por_km = tarifa_por_km
    self.__kilometraje = 0

  def calcular_tarifa(self, km):
    self.__kilometraje = km
    return self.__tarifa_por_km * km
  
  def devolver(self):
    # Reiniciar el km a 0 despues de delvolver
    super().devolver()
    self.__kilometraje = 0
    return "Vehiculo devuelto con exito. Kilometraje reiniciado"
  
  def mostrar_informacion(self):
    return f"{super().mostrar_informacion()}, Tarifa por km: {self.__tarifa_por_km}, Kilometraje: {self.__kilometraje}"
  