from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, precio_alquiler, cilindrada):
        super().__init__(marca, modelo, precio_alquiler)
        self.__cilindrada = cilindrada

    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Cilindrada: {self.__cilindrada}"
    