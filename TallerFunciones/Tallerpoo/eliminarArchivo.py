import os

def EliminarArchivo(RutaArchivo):
    RutaArchivo = input(r"Ingrese la ruta del archivo: ") # "D:\PORTAFOLIO SENA\Analisis y Desarrollo de Software\Segundo Trimestre\Python POO\TallerFunciones\Tallerpoo\temporal.txt"

    if os.path.exists(RutaArchivo):
        os.remove(RutaArchivo)
        print("El Archivo fue eliminado")
    else:
        print("No se ha Encontrado el Archivo")
    
EliminarArchivo()

#Retornar si es falso o verdadero