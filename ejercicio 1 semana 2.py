while True:
    print("--- Bienvenido a Menu--") 
    print("1 consultar")
    print("2 Registrar")
    print("3 salir")

    Respuesta = int(input("selecciona una opcion"))
    if Respuesta == 1:
        print("seleccionaste consulta")
    elif Respuesta ==2:
         print("seleccionaste registrar")
    elif Respuesta ==3 :
        print("seleccionaste salir")
         
        break
    else:
         print ("opcion equivocada")