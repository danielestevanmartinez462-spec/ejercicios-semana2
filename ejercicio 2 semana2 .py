clave = 1234

intento = int(input("Clave: "))
while intento != clave:
    print("Error")
    intento = int(input("Clave: "))
print("Bienvenido")