nu = int(input("Cuantos terminos desea ver: "))

a = 0
b = 1

for i in range(nu):
    print(a)
    siguiente = a + b
    a = b
    b = siguiente