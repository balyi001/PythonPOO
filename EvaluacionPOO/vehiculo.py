class Vehiculo:
    def __init__(self, marca, modelo, precio_alquiler, disponible=True):
        # Atributos privados
        self.__marca = marca
        self.__modelo = modelo
        self.__precio_alquiler = precio_alquiler
        self.__disponible = disponible

    # Retorna la información básica
    def mostrar_informacion(self):
        estado = "Si" if self.__disponible else "No"
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}, Precio: {self.__precio_alquiler}, Disponible: {estado}"

    # Cambia disponible a False
    def alquilar(self):
        if self.__disponible:
            self.__disponible = False
            return "Vehículo alquilado con éxito."
        return "El vehículo no está disponible."

    # Cambia disponible a True
    def devolver(self):
        self.__disponible = True
        return "Vehículo devuelto con éxito."

    # Setter para el precio
    def set_precio_alquiler(self, nuevo_precio):
        self.__precio_alquiler = nuevo_precio
        