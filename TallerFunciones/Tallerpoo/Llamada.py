def llamada(mensaje):
    print("Cordial saludo")
    print("Bienvenido")
    print(mensaje)

opcion = int(input("Ingrese una opcion...Entre 1 y 3"))

if opcion ==1:
    llamada('Elegiste la opcion 1')
elif opcion ==2:
    llamada('Elegiste la opcion 2')
else:
    print('La Opcion no es correcta')