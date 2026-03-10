# Importación de la clase base y sus tres especializaciones (subclases)
from carro import Carro
from carro_electrico import CarroElectrico
from carro_hibrido import CarroHibrido
from carro_deportivo import CarroDeportivo

# Línea decorativa para separar visualmente la ejecución en la consola
print("-" * 50)

# Instancia de la clase base. Solo tiene marca, color y velocidad máxima.
carro_gasolina = Carro("Mazda", "Rojo", 180)
print(carro_gasolina.encender())     # Activa el estado 'encendido'
print(carro_gasolina.acelerar(60))   # Aumenta la velocidad de forma estándar
print(carro_gasolina.frenar())       # Reduce la velocidad a 0
print(carro_gasolina, "\n")          # Muestra la representación __str__

print("-" * 50)

# Instancia con atributo adicional de batería (100)
carro_electrico = CarroElectrico("Tesla", "Negro", 250, 100)
print(carro_electrico.encender())
print(carro_electrico.acelerar(100)) # Acelera y consume batería
print(carro_electrico.acelerar(200)) 
print(carro_electrico.frenar())
print(carro_electrico, "\n")

print("-" * 50)

# Instancia con niveles de batería (1) y gasolina (87)
carro_hibrido = CarroHibrido("Toyota", "Blanco", 200, 1, 87)
print(carro_hibrido.encender())
# Aquí se activará la lógica de comparación: como gasolina > batería, usará gasolina
print(carro_hibrido.acelerar(50)) 
print(carro_hibrido.frenar())
print(carro_hibrido, "\n")

print("-" * 50)

# Instancia con nivel de combustible (55)
carro_deportivo = CarroDeportivo("Ferrari", "Rojo", 320, 55)
print(carro_deportivo.encender())
# Aquí se activará el multiplicador 'nitro' (50 * 2) y consumirá 10L de combustible
print(carro_deportivo.acelerar(50)) 
print(carro_deportivo.frenar())
print(carro_deportivo, "\n")