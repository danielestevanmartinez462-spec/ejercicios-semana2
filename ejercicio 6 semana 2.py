while True:
    Tipo = input("Ingrese su tipo de documento (cc, ti, ce): ")
    if Tipo == "cc":
        print("Seleccionaste Cedula de Ciudadania")
        break
    elif Tipo == "ti":
        print("Seleccionaste Tarjeta de Identidad")
        break
    elif Tipo == "ce":
        print("Seleccionaste Cedula de Extranjeria")
        break
    else:
        print("Opcion equivocada, intente de nuevo")
