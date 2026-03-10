from auto import Auto
from moto import Moto
from taxi import Taxi

# instancias
auto = Auto("Toyota", "Corolla", 50000, 4)
moto = Moto("Yamaha", "R3", 30000, "300cc")
taxi = Taxi("Hyundai", "Accent", 60000, 5000)

print("=" * 50, "\n")

print(auto.mostrar_informacion())
print(auto.alquilar())
print(auto.mostrar_informacion())
print(auto.devolver())
print(auto.mostrar_informacion(), "\n")

print("=" * 50, "\n")

print(moto.mostrar_informacion())
print(moto.alquilar())
print(moto.mostrar_informacion())
print(moto.devolver())
print(moto.mostrar_informacion(), "\n")

print("=" * 50, "\n")

print(taxi.mostrar_informacion())
print(taxi.alquilar())
pago = taxi.calcular_tarifa(15)
print(f"Costo del viaje en taxi por 15 km: {pago}")
print(taxi.mostrar_informacion())
print(taxi.devolver())
print(taxi.mostrar_informacion(), "\n")

print("=" * 50, "\n")
