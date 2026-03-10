from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, precio_alquiler, num_puertas):
        super().__init__(marca, modelo, precio_alquiler)
        self.__num_puertas = num_puertas

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Número de puertas: {self.__num_puertas}"
    