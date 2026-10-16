Total = 0
while True:
    Numero = float(input("Ingrese un numero (0 para terminar): "))
    if Numero == 0:
        print("La suma total es:", Total)
        break
    else:
        Total = Total + Numero