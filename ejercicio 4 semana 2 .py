nota = float(input("Ingrese la nota: "))
while nota < 0 or nota > 5:
    print("Nota invalida, debe estar entre 0.0 y 5.0")
    nota = float(input("Ingrese la nota: "))
print("Nota valida:", nota)