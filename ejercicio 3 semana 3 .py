clave = 1234
intentos = 1

intento = int(input("Clave: "))
while intento != clave and intentos < 3:
    print("Error")
    intento = int(input("Clave: "))
    intentos = intentos + 1

if intento == clave:
    print("Acceso concedido")
else:
    print("Cuenta bloqueada")