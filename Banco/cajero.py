import random
#creamos la clase principal 
class CuentaCorriente:
    # se declara el Inicio
    def __init__(self, nombre: str, saldo: float):
        self.nombre = nombre
        self.saldo = saldo
        self.numero_cuenta = abs(random.randint(0,10**9))
    #se declara metodo para el ingreso y validacion
    def set_ingreso(self, ingreso:float):
        if ingreso <=0:
            print("no se permiten ingresos negativos.")
        else:
            self.saldo += ingreso
            print("tranferencia realizada con exito")
    # se declara el metodo para el retiro y validacion con el saldo actual
    def set_retiro(self,retiro:float):
        if retiro > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -=retiro
            print("Retiro exitoso")
    #retornar el salfo acctual de la ccuenta 
    def get_saldo(self)->str:
        return f"el saldo de la cuenta es:{self.saldo}"
    
    #Realizar el procedimiento para realizar una tranferencia 
    @staticmethod
    def transferencia(titular1,titular2,cantidad :float):
        if cantidad>titular1.saldo:
            print("Fondos insuficientes para la trasnferencia"  )
        else:
            titular2.saldo+=cantidad
            titular1.saldo-=cantidad
            print("Tranferencia realizada con exito")
    #mostrar todos los datos de la cuenta 
    def get_datos_cuenta(self)->str:
        return f"Titular: {self.nombre}\n Numero de cuenta: {self.numero_cuenta} \n Saldo: {self.saldo}"